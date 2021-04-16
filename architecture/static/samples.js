// JavaScript code goes here

// use the Luxon library to handle dates and times nicely (loaded as a script into index.html)
const DateTime = luxon.DateTime

// we need models so we can persist data here (on the web browser client)
let historic_values = [] // an empty array
let start_dt
let end_dt
let urlStr
let alert_start_dt
let alert_end_dt
let showOriginal = flexSwitchCheckDefault.checked //  is the switch on (true) or off (false)
let chartT // this will be our 'highcharts' chart



// function to plot chart using historical data
const makeChart = (chart_data) => {
    seriesSensorData = []
    seriesDiffData = []
    // create plotable data structures for each sensor data, both actual and abs difference series
    for (let i=0; i<5; i++){
        seriesSensorData.push(JSON.parse(chart_data[i]))
        // now loop over this series and grab the SECOND set of values (ie the difference values)
        diffSeries = [[seriesSensorData[i][0][0], 0]] // we know the first value must have a diff of zero
        // we've already set member zero to '0' so start from member 1
        for (let j=1; j<seriesSensorData[i].length; j++){
            diffSeries.push([seriesSensorData[i][j][0], seriesSensorData[i][j][2]])
        }
        seriesDiffData.push(diffSeries)
    }
    // console.log(seriesDiffData)
    chartT = new Highcharts.Chart({
        // turboThreshold:9999, // https://api.highcharts.com/highcharts/plotOptions.series.turboThreshold
        chart: { renderTo: 'sample-chart' },
        title: { text: 'Sample Change in FSR data' },
        series: [
            // sensor 1 
            {
                name: 'Sensor 1 reading',
                type: 'line',
                yAxis: 0,
                showInLegend: true,
                data: seriesSensorData[0]
            },
            {
                name: 'Sensor 1 abs diff',
                type: 'spline',
                yAxis: 1,
                showInLegend: true,
                data: seriesDiffData[0]
            },
            // sensor 2
            {
                name: 'Sensor 2 reading',
                type: 'line',
                yAxis: 0,
                showInLegend: true,
                data: seriesSensorData[1]
            },
            {
                name: 'Sensor 2 abs diff',
                type: 'spline',
                yAxis: 1,
                showInLegend: true,
                data: seriesDiffData[1]
            },
            // sensor 3
            {
                name: 'Sensor 3 reading',
                type: 'line',
                yAxis: 0,
                showInLegend: true,
                data: seriesSensorData[2]
            },
            {
                name: 'Sensor 3 abs diff',
                type: 'spline',
                yAxis: 1,
                showInLegend: true,
                data: seriesDiffData[2]
            },
            // sensor 4
            {
                name: 'Sensor 4 reading',
                type: 'line',
                yAxis: 0,
                showInLegend: true,
                data: seriesSensorData[3]
            },
            {
                name: 'Sensor 4 abs diff',
                type: 'spline',
                yAxis: 1,
                showInLegend: true,
                data: seriesDiffData[3]
            },
            // sensor 5
            {
                name: 'Sensor 5 reading',
                type: 'line',
                yAxis: 0,
                showInLegend: true,
                data: seriesSensorData[4]
            },
            {
                name: 'Sensor 5 abs diff',
                type: 'spline',
                yAxis: 1,
                showInLegend: true,
                data: seriesDiffData[4]
            }
        ],
        plotOptions: {
            line: {
                animation: false,
                dataLabels: { enabled: true }
            },
            // series: { colors: ['#ff0000', '#00ff00', '#0000ff', '#f9933', '#3399ff'] } // color each line differently
        },
        xAxis: {
            type: 'datetime',
            // dateTimeLabelFormats:{ second: '%H:%M:%S' }, //days:'%d %b %Y', 
            labels: {
                formatter: function () { // caution: we MUST use 'function' here rther than the newer ()=>{} in order to have 'this.value' in scope
                    // return Highcharts.dateFormat('%H:%M:%S %d %b %Y', this.value);
                    // console.log(this) // a compl
                    id = this.value // this.value is the data id number 1, 2, 3 etc.
                    dt = JSON.parse(chart_data[0])[id][0] // grab the date label from the original data
                    return dt
                }
            }
        },
        yAxis: [
            { // Primary yAxis
                labels: {
                    format: '{value}',
                    style: {
                        color: Highcharts.getOptions().colors[1]
                    }
                },
                title: {
                    text: 'Sensor Reading',
                    style: {
                        color: Highcharts.getOptions().colors[1]
                    }
                }
            }, { // Secondary yAxis
                title: {
                    text: 'Absolute Difference',
                    style: {
                        color: Highcharts.getOptions().colors[0]
                    }
                },
                labels: {
                    format: '{value}',
                    style: {
                        color: Highcharts.getOptions().colors[0]
                    }
                },
                opposite: true
            }],
        credits: { enabled: false }
    })
    // visibility of chart series - initially just show the differences
    for (var i =0; i < chartT.series.length; i+=2){
        chartT.series[i].setVisible(false, false); 
    }  
    chartT.redraw()
}

const toggleDataVisible = ()=>{
    showOriginal = flexSwitchCheckDefault.checked
    for (var i =0; i < chartT.series.length; i+=2){
        chartT.series[i].setVisible(showOriginal, false); 
    }  
    chartT.redraw()
}

// a function to retrieve data from the db via Python
const fetchDTResults = (start_dt, end_dt) => {
    urlStr = `http://127.0.0.1:5000/retrieve?start_dt=${start_dt}&end_dt=${end_dt}`
    // console.log(urlStr) // the dt values are UTC (not SQL)
    fetch(urlStr)
        .then(
            response => response.text() // or response.json?
        ).then(
            (data_j) => {
                // now we need to un-pack the returned JSON into data we can use in the browser
                historic_values = JSON.parse(data_j) // convert the json to data structures
                // use these values in a chart
                makeChart(historic_values)
            }
        )
}

const handlePilot = () => {
    // known-good data from 17 March 2021
    start_dt = "2021-03-17 14:42:45"
    end_dt = "2021-03-17 14:42:55"
    // pass these date-times to our generic 'fetcher' function
    fetchDTResults(start_dt, end_dt)
}

const handleOvernight = () => {
    // known-good data from overnight on 5 sensors
    start_dt = "2021-03-04 14:30:25"
    end_dt = '2021-03-04 16:53:23'

    // pass these date-times to our generic 'fetcher' function
    fetchDTResults(start_dt, end_dt)
}
const handleEleven = () => {
    // known-good data from eleven seizure emulations
    start_dt = '2021-03-03 14:42:55'
    end_dt = '2021-03-03 15:05:37'
    // pass these date-times to our generic 'fetcher' function
    fetchDTResults(start_dt, end_dt)
}
// listen out for 'click' events
btnOvernight.addEventListener('click', handleOvernight)
btnEleven.addEventListener('click', handleEleven)
btnPilot.addEventListener('click', handlePilot)

flexSwitchCheckDefault.addEventListener('change', toggleDataVisible)

// init method (gets called later)
const init = () => {
    // set date and time field values to sensible defaults by using the Luxon library
    let currentDate = new Date()
    currentDate.setSeconds(0, 0) // remove any seconds and milliseconds
}

// do some initilization when the page first loads
document.addEventListener("DOMContentLoaded", init);
