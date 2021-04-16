let showOriginal = flexSwitchCheckDefault.checked
let chartT = new Highcharts.Chart({
    chart: { renderTo: 'movement-chart' },
    title: { text: 'Change in FSR data' },
    series:[
        // sensor 1 
        {
            name: 'Sensor 1 reading',
            type: 'line',
            yAxis: 0,
            showInLegend: true,
            data: []
        },
        {
            name: 'Sensor 1 abs diff',
            type: 'spline',
            yAxis: 1,
            showInLegend: true,
            data: []
        },
        // sensor 2
        {
            name: 'Sensor 2 reading',
            type: 'line',
            yAxis: 0,
            showInLegend: true,
            data: []
        },
        {
            name: 'Sensor 2 abs diff',
            type: 'spline',
            yAxis: 1,
            showInLegend: true,
            data: []
        },
        // sensor 3
        {
            name: 'Sensor 3 reading',
            type: 'line',
            yAxis: 0,
            showInLegend: true,
            data: []
        },
        {
            name: 'Sensor 3 abs diff',
            type: 'spline',
            yAxis: 1,
            showInLegend: true,
            data: []
        },
        // sensor 4
        {
            name: 'Sensor 4 reading',
            type: 'line',
            yAxis: 0,
            showInLegend: true,
            data: []
        },
        {
            name: 'Sensor 4 abs diff',
            type: 'spline',
            yAxis: 1,
            showInLegend: true,
            data: []
        },
        // sensor 5
        {
            name: 'Sensor 5 reading',
            type: 'line',
            yAxis: 0,
            showInLegend: true,
            data: []
        },
        {
            name: 'Sensor 5 abs diff',
            type: 'spline',
            yAxis: 1,
            showInLegend: true,
            data: []
        }
    ],
    plotOptions: {
        line: {
            animation: false,
            dataLabels: { enabled: true }
        },
        // series: { color: '#059e8a' }
        // series: { colors: ['#059e8a', '#c0ffee', '#c0ac0a', '#f9933', '#3399ff'] } // color each line differently
    },
    xAxis: {
        type: 'datetime',
        dateTimeLabelFormats: { second: '%H:%M:%S' }
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
});
setInterval(() => { // replaced old-skool 'function' with modern ()=>{} syntax)
    prev0 = prev1 = prev2 = prev3 = prev4 = 0 // reset the initial values to zero
    fetch('http://192.168.0.40/movement')
        .then(response => response.text()) // convert the data from JSON
        .then(
            // when the data comes back, put in into the page
            (data) => {
                data_arr = data.split('-')
                console.log(data_arr[0], data_arr[1])
                let x = (new Date()).getTime()
                y0 = parseFloat(data_arr[0]);
                y1 = parseFloat(data_arr[1]);
                y2 = parseFloat(data_arr[2]);
                y3 = parseFloat(data_arr[3]);
                y4 = parseFloat(data_arr[4]);
                // we also need the absolute differences
                d0 = abs(y0-prev0)
                prev0 = d0
                d1 = abs(y1-prev1)
                prev1 = d1
                d2 = abs(y2-prev2)
                prev2 = d2
                d3 = abs(y3-prev3)
                prev3 = d3
                d4 = abs(y4-prev4)
                prev4 = d4
                // instead of if...else we just check the length is under 50 to return true or false
                chartT.series[0].addPoint([x, y0], true, chartT.series[0].data.length < 50, true);
                chartT.series[2].addPoint([x, y1], true, chartT.series[0].data.length < 50, true);
                chartT.series[4].addPoint([x, y2], true, chartT.series[0].data.length < 50, true);
                chartT.series[6].addPoint([x, y3], true, chartT.series[0].data.length < 50, true);
                chartT.series[8].addPoint([x, y4], true, chartT.series[0].data.length < 50, true);
                // here's the differences
                chartT.series[1].addPoint([x, y0], true, chartT.series[0].data.length < 50, true);
                chartT.series[3].addPoint([x, y1], true, chartT.series[0].data.length < 50, true);
                chartT.series[5].addPoint([x, y2], true, chartT.series[0].data.length < 50, true);
                chartT.series[7].addPoint([x, y3], true, chartT.series[0].data.length < 50, true);
                chartT.series[9].addPoint([x, y4], true, chartT.series[0].data.length < 50, true);
            })
}, 1000);

const toggleDataVisible = ()=>{
    showOriginal = flexSwitchCheckDefault.checked
    for (var i =0; i < chartT.series.length; i+=2){
        chartT.series[i].setVisible(showOriginal, false); 
    }  
    chartT.redraw()
}

flexSwitchCheckDefault.addEventListener('change', toggleDataVisible)

