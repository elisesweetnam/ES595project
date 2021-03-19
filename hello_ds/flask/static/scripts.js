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

// a function to retrieve data from the db via Python
const fetchDTResults=(start_dt, end_dt)=>{
    // for now we send some sensible defaults
    // start_dt='2021-03-04 17:00:00'
    // end_dt='2021-03-04 17:00:30'
    // make sure the date-time values are compatible with what SQL expects
    // see the formatting tokens here https://moment.github.io/luxon/docs/manual/formatting.html
    let start_dt_sql = DateTime.fromISO(start_dt).toFormat('yyyy-LL-dd HH:mm:ss')
    let end_dt_sql = DateTime.fromISO(end_dt).toFormat('yyyy-LL-dd HH:mm:ss')

    urlStr = `http://127.0.0.1:5000/retrieve?start_dt=${start_dt_sql}&end_dt=${end_dt_sql}`
    console.log(urlStr) // see teh dt values are UTC (not SQL)
    fetch(urlStr)
        .then(
            response => response.text() // or response.json?
        ).then(
            (data) => {
                console.log(data) // see the returned data in the browser console
                monitor.value = data // write the data into the page
                // now we need to un-pack the returned JSON into data we can use in the browser
                historic_values = JSON.parse(data) // convert the json to data structures
                console.log(historic_values) // lets see what we have
                // go ahead an use these values in a chart ......ummmmmmm
            }
        )    
}

const handleUserDT=()=>{
    // grab whatever dates the user has chosen for start_dt and end_dt
    start_dt = min_date.value
    end_dt = max_date.value
    // pass them to our generic dat-time handler
    fetchDTResults(start_dt, end_dt)
}

// use the luxon library to do date-time calculations
// see https://moment.github.io/luxon/docs/manual/tour.html
const handle5Mins=()=>{
    let now = DateTime.now()
    let ago5mins = now.minus({ minutes: 5 });
    start_dt=ago5mins
    end_dt=now
    // pass these to our generic fetcher
    fetchDTResults(start_dt, end_dt)
}

const handleLastAlert=()=>{
    // retrieve the data related to teh most recent alert
    start_dt=alert_start_dt // no values yet...
    end_dt=alert_end_dt
    // pass these to our generic fetcher
    fetchDTResults(start_dt, end_dt)
}

// use the luxon library to do date-time calculations
// see https://moment.github.io/luxon/docs/manual/tour.html
const handleHour=()=>{
    let now = DateTime.now()
    let ago1Hour = now.minus({ hours: 1 });
    start_dt=ago1Hour
    end_dt=now
    // pass these to our generic fetcher
    fetchDTResults(start_dt, end_dt)
}

// use the luxon library to do date-time calculations
// see https://moment.github.io/luxon/docs/manual/tour.html
const handleDay=()=>{
    let now = DateTime.now()
    let ago1Day = now.minus({ days: 1 });
    start_dt=ago1Day
    end_dt=now
    // pass these to our generic 'fetcher' function
    fetchDTResults(start_dt, end_dt)
}

const handleRecentMinutes=()=>{
    // every time there is a change to the 'recentMinutes' range, update the historical results
    let numMinutes= recentMinutes.value
    recentMinutesLabel.innerHTML = numMinutes
}

// listen out for 'click' events
btnGetData.addEventListener('click', handleUserDT)
btnLastDay.addEventListener('click', handleDay)
btnLastHour.addEventListener('click', handleHour)
btnLast5Mins.addEventListener('click', handle5Mins)
btnLastAlert.addEventListener('click', handleLastAlert)
// listen out for a 'change' event
recentMinutes.addEventListener('change', handleRecentMinutes) //for the slider 

// init method (gets called later)
const init=()=>{
    // set form values to sensible defaults
    // sets dates to current date
    min_date.valueAsDate = new Date()
    max_date.valueAsDate = new Date()
    min_time.valueAsDate = new Date()
    max_time.valueAsDate = new Date()
}

// do some initilization when the page first loads
document.addEventListener("DOMContentLoaded", init);
