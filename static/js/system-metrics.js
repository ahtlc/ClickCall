var ctx = document.getElementById('callChart').getContext('2d');
const chart = new Chart(ctx,{
    type: 'line',        
    options:{
      layout: {
        padding: {
          left: 10,
          right: 10,
          top: 20,
          bottom: 20
        },
      },
      legend: {
          display: false
      },
    }
  });
$(document).ready(function(){
  var filterby ='yearly';
  constructChart(filterby);
});

function constructChart(filterby){
  $.ajax({
    url: '/activities/getdata?filterby='+filterby,
    type: "GET",
    dataType: "json",
    success: function (data) {
        let chartData = constructChartData(data, filterby);
        chart.data.datasets = chartData.datasets;
        chart.data.labels = chartData.labels;
        chart.update();
    }
  });
}

function constructChartData(data, filterby){
  let labels = [];
  let received = {
        data : [],
        label: 'Recebidas',
        borderColor: '#F8BD1D',
        backgroundColor: '#F8BD1D',
        lineTension: 0,
        fill:false,
        borderWidth: 1,
      };
  let answered = {
        data : [],
        label: 'Atendidas',
        borderColor: '#4ABE57',
        backgroundColor: '#4ABE57',
        lineTension: 0,
        fill:false,
        borderWidth: 1,
      };
  let declined = {
        data : [],
        label: 'Abandonadas',
        borderColor: '#F03B3B',
        backgroundColor: '#F03B3B',
        lineTension: 0,
        fill:false,
        borderWidth: 1,
      };
  let not_answered = {
        data : [],
        label: 'Não atendidas',
        borderColor: '#FF9F2F',
        backgroundColor: '#FF9F2F',
        lineTension: 0,
        fill:false,
        borderWidth: 1,
  };
  data.forEach(element => {
    if(filterby=='yearly'){
      labels.push(element.year);
    }
    else if(filterby=='daily'){
      labels.push(element.date.day+'/'+element.date.month+'/'+element.date.year);
    }
    else{
      labels.push(element.month+'/'+element.year);
    }
    received.data.push(element.received);
    answered.data.push(element.answered);
    declined.data.push(element.declined);
    not_answered.data.push(element.not_answered);
  });
  let datasets = [received,answered,declined,not_answered];
  return {
    datasets: datasets,
    labels: labels
  }
}

function filterChart(filterby){
  constructChart(filterby);
  document.getElementById('yearly-filter').style.color="#4D4D4D";
  document.getElementById('monthly-filter').style.color="#4D4D4D";
  document.getElementById('daily-filter').style.color="#4D4D4D";
  document.getElementById(filterby+'-filter').style.color="#27B2FF";
}