<!DOCTYPE html>
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>SB Admin - Dashboard</title>

    <!-- Bootstrap core CSS-->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom fonts for this template-->
    <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">

    <!-- Page level plugin CSS-->
    <link href="vendor/datatables/dataTables.bootstrap4.css" rel="stylesheet">

    <!-- Custom styles for this template-->
    <link href="css/sb-admin.css" rel="stylesheet">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

  </head>

  <body id="page-top" onclick="myFunction(event)">
	

    <?php require 'navbar.php'; ?>

    <div id="wrapper">

      <!-- Sidebar -->
      <ul class="sidebar navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" href="index.php">
            <i class="fas fa-fw fa-tachometer-alt"></i>
            <span>Dashboard</span>
          </a>
        </li>
        <li class="nav-item dropdown">
    
        </li>
        <li class="nav-item">
          <a class="nav-link" href="jour.php">
            <i class="fas fa-fw fa-chart-area"></i>
            <span>Jour</span></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="mois.php">
            <i class="fas fa-fw fa-chart-area"></i>
            <span>Mois</span></a>
        </li>
<li class="nav-item">
          <a class="nav-link" href="annee.php">
            <i class="fas fa-fw fa-chart-area"></i>
            <span>Année</span></a>
        </li>
      </ul>

      <div id="content-wrapper">

        <div class="container-fluid">

          <!-- Breadcrumbs-->
          <ol class="breadcrumb">
            <li class="breadcrumb-item">
              <a href="#">Dashboard</a>
            </li>
            <li class="breadcrumb-item active">Accueil</li>
          </ol>

          <!-- Icon Cards-->
		  <script>
		  window.onload = function () {
		  //annee
		  $.ajax({
            url:"http://thomasfaure05.alwaysdata.net/php/infosAnnee.php",
            async : false,
            method:"POST",
            success:function(response) {
				var obj = JSON.parse(response);
                datas=obj;
				var e = document.getElementById("annee");
				var quantiteTotale=0;
				for(var i=0;i<datas.length;i=i+1){
					quantiteTotale=quantiteTotale+parseInt(datas[i]["quantite"]);
				}
		e.innerHTML=quantiteTotale+' Feuille(s) ont été distribuées cette année';
				
            },
            error:function(){
                alert("error");

            }
		
        });
		  //mois
		  $.ajax({
            url:"http://thomasfaure05.alwaysdata.net/php/infosMois.php",
            async : false,
            method:"POST",
            success:function(response) {
				var obj = JSON.parse(response);
                datas=obj;
				var e = document.getElementById("mois");
				var quantiteTotale=0;
				for(var i=0;i<datas.length;i=i+1){
					quantiteTotale=quantiteTotale+parseInt(datas[i]["quantite"]);
				}
		e.innerHTML=quantiteTotale+' Feuille(s) ont été distribuées ce mois-ci';
				
            },
            error:function(){
                alert("error");

            }
		
        });
		//jour
		  $.ajax({
            url:"http://thomasfaure05.alwaysdata.net/php/infosJour.php",
            async : false,
            method:"POST",
            success:function(response) {
				var obj = JSON.parse(response);
                datas=obj;
				var e = document.getElementById("jour");
		e.innerHTML=datas[0]["quantite"]+' Feuille(s) ont été distribuées aujourd\'hui';
				
            },
            error:function(){
                alert("error");

            }

        });
	
	};

	  
		  </script>
          <div  class="row">
            <div class="col-xl-4 col-sm-6 mb-3">
              <div class="card text-white bg-primary o-hidden h-100">
                <div class="card-body">
                  <div class="card-body-icon">
                    <i class="fas fa-fw fa-comments"></i>
                  </div>
                  <div id="jour" class="mr-5">chargement</div>
                </div>
                <a class="card-footer text-white clearfix small z-1" href="jour.php">
                  <span class="float-left">Plus de détails</span>
                  <span class="float-right">
                    <i class="fas fa-angle-right"></i>
                  </span>
                </a>
              </div>
            </div>
            <div class="col-xl-4 col-sm-6 mb-3">
              <div class="card text-white bg-warning o-hidden h-100">
                <div class="card-body">
                  <div class="card-body-icon">
                    <i class="fas fa-fw fa-comments"></i>
                  </div>
                  <div class="mr-5" id="mois">chargement</div>
                </div>
                <a class="card-footer text-white clearfix small z-1" href="mois.php">
                  <span class="float-left">Plus de détails</span>
                  <span class="float-right">
                    <i class="fas fa-angle-right"></i>
                  </span>
                </a>
              </div>
            </div>
            <div class="col-xl-4 col-sm-6 mb-3">
              <div class="card text-white bg-success o-hidden h-100">
                <div class="card-body">
                  <div class="card-body-icon">
                    <i class="fas fa-fw fa-comments"></i>
                  </div>
                  <div id="annee" class="mr-5">chargement</div>
                </div>
                <a class="card-footer text-white clearfix small z-1" href="annee.php">
                  <span class="float-left">Plus de détails</span>
                  <span class="float-right">
                    <i class="fas fa-angle-right"></i>
                  </span>
                </a>
              </div>
            </div>
          </div>

          <!-- Area Chart Example-->
          <div class="card mb-3">
            <div class="card-header">
              <i class="fas fa-chart-area"></i>
              Consommations durant les 5 derniers jours</div>
            <div class="card-body">
              <canvas id="myAreaChart" width="100%" height="30"></canvas>
            </div>
            <div class="card-footer small text-muted">Denière mise à jour : Maintenant</div>
          </div>

         
        <!-- /.container-fluid -->

        <!-- Sticky Footer -->
        <footer class="sticky-footer">
          <div class="container my-auto">
            <div class="copyright text-center my-auto">
              <span>Copyright © Your Website 2018</span>
            </div>
          </div>
        </footer>

      </div>
      <!-- /.content-wrapper -->

    </div>
    <!-- /#wrapper -->

    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
      <i class="fas fa-angle-up"></i>
    </a>

    <!-- Logout Modal-->
    <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
            <button class="close" type="button" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">×</span>
            </button>
          </div>
          <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
          <div class="modal-footer">
            <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
            <a class="btn btn-primary" href="login.html">Logout</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Bootstrap core JavaScript-->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Core plugin JavaScript-->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Page level plugin JavaScript-->
    <script src="vendor/chart.js/Chart.min.js"></script>
    <script src="vendor/datatables/jquery.dataTables.js"></script>
    <script src="vendor/datatables/dataTables.bootstrap4.js"></script>

    <!-- Custom scripts for all pages-->
    <script src="js/sb-admin.min.js"></script>

    <!-- Demo scripts for this page-->
    <script src="js/demo/datatables-demo.js"></script>
    <script src="js/Chart_area_jour.js"></script>

  </body>

</html>
