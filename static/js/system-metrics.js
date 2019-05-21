$(document).ready(function(){
  var filterby ='monthly';

  $.ajax({
    url: '/activities/getdata?filterby='+filterby,
    type: "GET",
    dataType: "json",
    success: function (data) {
        console.log(data);
        console.log(data.length);
        let labels = [];
        let datasets = [];
        let dataset = {
          data : []
        };
        data.forEach(element => {
          if(filterby=='yearly'){
            labels.push(element.date.year);
          }
          else if(filterby=='daily'){
            labels.push(element.date.day+'/'+element.date.month+'/'+element.date.year);
          }
          else{
            labels.push(element.month+'/'+element.year);
          }
          dataset.data.push(element.calls);
        });
        var ctx = document.getElementById('myChart').getContext('2d');
        var chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'My First dataset',
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: dataset.data
                }]
            },

            // Configuration options go here
            options: {}
        });
    }
    });
});