// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';


// Pie Chart Example
var datas;
$.ajax({
    url:"http://thomasfaure05.alwaysdata.net/php/infosAnnee.php",
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

tab=[];
tab[1]=0;
tab[2]=0;
tab[3]=0;
tab[4]=0;
tab[5]=0;
tab[6]=0;
tab[7]=0;
tab[8]=0;
tab[9]=0;
tab[10]=0;
tab[11]=0;
tab[12]=0;
for(var i=0;i<datas.length;++i){
    tab[datas[i]["mois"]]=tab[datas[i]["mois"]]+parseInt(datas[i]["mois"]);
}


// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["janvier", "fevrier", "mars", "avril","mai", "juin", "juillet", "aout","septembre", "octobre", "novembre", "decembre"],
        datasets: [{
            label: "feuilles déroulées",
            backgroundColor: "rgba(2,117,216,1)",
            borderColor: "rgba(2,117,216,1)",
            data: [tab[1], tab[2], tab[3],tab[4], tab[5], tab[6], tab[7],tab[8], tab[9], tab[10], tab[11],tab[12]],
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
