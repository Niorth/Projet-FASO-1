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
var total = 0;
for(var i=0;i<datas.length;++i){
    total = total + parseInt(datas[i]["mois"]);
}
for(var i=0;i<datas.length;++i){
    tab[datas[i]["mois"]]=tab[datas[i]["mois"]]+parseInt(datas[i]["mois"]);
}

var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ["janvier", "fevrier", "mars", "avril","mai", "juin", "juillet", "aout","septembre", "octobre", "novembre", "decembre"],
        datasets: [{
            data: [Math.round(tab[1]*100/total), Math.round(tab[2]*100/total), Math.round(tab[3]*100/total),Math.round(tab[4]*100/total), Math.round(tab[5]*100/total), Math.round(tab[6]*100/total), Math.round(tab[7]*100/total),Math.round(tab[8]*100/total), Math.round(tab[9]*100/total), Math.round(tab[10]*100/total), Math.round(tab[11]*100/total),Math.round(tab[12]*100/total)],
            backgroundColor: ['#F20028', '#F20099', '#D900F2', '#6900F2','#0010F2', '#00B9F2', '#00F291', '#28a745','#007bff', '#46EA00', '#EAEA00', '#EA8D00'],
        }],
    },
});
