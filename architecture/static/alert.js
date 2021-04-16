// use the Luxon library to handle dates and times nicely (loaded as a script into index.html)
const DateTime = luxon.DateTime
// we need models so we can persist data here (on the web browser client)
let historic_values = [] // an empty array
let start_dt
let end_dt
let urlStr
let alert_start_dt
let alert_end_dt

// function to plot chart using historical data
const makeChart = (chart_data)=>{
    // console.log(Date(JSON.parse(chart_data[0])[0][0]))
    // we do need to decide if the chart neds a 'max size'
    let chartT = new Highcharts.Chart({
        // turboThreshold:9999, // https://api.highcharts.com/highcharts/plotOptions.series.turboThreshold
        chart:{ renderTo : 'alert-chart' },
        title: { text: 'Alert Data' },
        series: [{
            // need a way to grab the date part as a DATE (currently just a value 1-111)
            // data: [{x: (new Date(JSON.parse(chart_data[0])[0][0])).getTime(), y: JSON.parse(chart_data[0])[0][1]}], // JSON.parse(chart_data[0])[0][1]}],
            name:'Sensor 1',
            showInLegend: true,
            data: JSON.parse(chart_data[0]) // e.g. ["2021-03-17 14:42:16.287826", 1530]
            // takes string and converts into an array 
         }
        ,{
            name:'Sensor 2',
            showInLegend: true,
            data: JSON.parse(chart_data[1])
        },
        {
            name:'Sensor 3',
            showInLegend: true,
            data: JSON.parse(chart_data[2])
        },
        {
            name:'Sensor 4',
            showInLegend: true,
            data: JSON.parse(chart_data[3])
        },
        {
            name:'Sensor 5',
            showInLegend: true,
            data: JSON.parse(chart_data[4])
        }
        ],
        plotOptions: {
            line: { animation: false,
            dataLabels: { enabled: true }
            },
            // series: { colors: ['#ff0000', '#00ff00', '#0000ff', '#f9933', '#3399ff'] } // color each line differently
        },
        xAxis: { 
                type: 'datetime',
                // dateTimeLabelFormats:{ second: '%H:%M:%S' }, //days:'%d %b %Y', 
                labels: {
                    formatter: function(){ // caution: we MUST use 'function' here rther than the newer ()=>{} in order to have 'this.value' in scope
                        // return Highcharts.dateFormat('%H:%M:%S %d %b %Y', this.value);
                        // console.log(this) // a compl
                        id = this.value // this.value is the data id number 1, 2, 3 etc.
                        dt = JSON.parse(chart_data[0])[id][0] // grab the date label from the original data
                        return dt
                    }
                }
        },
        yAxis: {
        },
        credits: { enabled: false }
    });
}

// a function to retrieve data from the db via Python
const fetchDTResults=(start_dt, end_dt)=>{
    urlStr = `http://127.0.0.1:5000/retrieve?start_dt=${start_dt}&end_dt=${end_dt}`
    // console.log(urlStr) // the dt values are UTC (not SQL)
    fetch(urlStr)
        .then(
            response => response.text() // or response.json?
        ).then(
            (data_j) => {
                // now we need to un-pack the returned JSON into data we can use in the browser
                historic_values = JSON.parse(data_j) // convert the json to data structures
                // console.log(historic_values) 
                // use these values in a chart
                makeChart(historic_values)
            }
        )    
}

const handleLastAlert=()=>{
    // parse the json received with the page
    data_j = JSON.parse(data)
    console.log(data_j)
    // retrieve the data related to the most recent alert
    start_dt=data.start_dt
    end_dt=data.end_dt
    // pass these to our generic fetcher
    // fetchDTResults(start_dt, end_dt)
    makeChart(data)
}

const init = ()=>{
    // do any initialization here
    handleLastAlert()
}

// do some initilization when the page first loads
// document.addEventListener("DOMContentLoaded", init);
window.onload = init()