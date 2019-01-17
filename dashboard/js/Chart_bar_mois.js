// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';


// Pie Chart Example
var datas;
$.ajax({
    url:"http://thomasfaure05.alwaysdata.net/php/infosMois.php",
    async : false,
    method:"POST",
    success:function(response) {
        var obj = JSON.parse(response);
        //alert(obj);
        datas=obj;
    },
    error:function(){
        alert("error");

    }

});
var premier=0;
var deuxieme=0;
var troisieme=0;
var quatrieme=0;
for(var i=0;i<datas.length;++i){
    if(datas[i]["jour"]<8){

        premier=premier+parseInt(datas[i]["jour"]);
    }else if(datas[i]["jour"]<16){
        deuxieme=deuxieme+parseInt(datas[i]["jour"]);
    }else if (datas[i]["jour"]<24){
        troisieme=troisieme+parseInt(datas[i]["jour"]);
    }else{
        quatrieme=quatrieme+parseInt(datas[i]["jour"]);
    }
}

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["1ère semaine", "2ième semaine", "3ième semaine", "4ième semaine"],
        datasets: [{
            label: "feuilles déroulées",
            backgroundColor: "rgba(2,117,216,1)",
            borderColor: "rgba(2,117,216,1)",
            data: [premier, deuxieme, troisieme, quatrieme],
        }],
    },
    options: {
        scales: {
            xAxes: [{
                time: {
                    unit: 'month'
                },
                gridLines: {
                    display: false
                },
                ticks: {
                    maxTicksLimit: 6
                }
            }],
            yAxes: [{
                ticks: {
                    min: 0,
                    max: 200,
                    maxTicksLimit: 5
                },
                gridLines: {
                    display: true
                }
            }],
        },
        legend: {
            display: false
        }
    }
});
