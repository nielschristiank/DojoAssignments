


$(document).ready(function() {

  var API_KEY = "b9080645768c9c5bfd3f17b2d0498d3a";

  $('form').submit(function() {
    var city = $("#city").val();
    $("#city").val("");
    console.log(city);
    var weather_current = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&appid=" + API_KEY;
    $.get(weather_current, function(weather) {
      console.log(weather);
      var current_temp = weather.main.temp;
      var desc = weather.weather[0].description;
      var humid = weather.main.humidity;
      var hi_temp = weather.main.temp_max;
      var lo_temp = weather.main.temp_min;
      var weatherHtmlString = "<h1>" + city + "</h1><div id='current'>";
      weatherHtmlString += "<h2>Currently</h2><h3>" + desc + "</h3><h4>" + current_temp + " F &#176;</h4>";
      weatherHtmlString += "<h4>" + humid + " % humidity</h4></div>";
      weatherHtmlString += "<div id='high_low'><div><h2>High</h2><h4>" + hi_temp + " F &#176;</h4></div>";
      weatherHtmlString += "<div id='high_low'><div><h2>Low</h2><h4>" + lo_temp + " F &#176;</h4></div></div>";

      $('#today_weather').html(weatherHtmlString);
    }, "json");
    return false;
  });

});
