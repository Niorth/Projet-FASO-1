
<nav class="navbar navbar-expand navbar-dark bg-dark static-top">

      <a class="navbar-brand mr-1" href="index.html">Distributeur</a>

      <button class="btn btn-link btn-sm text-white order-1 order-sm-0" id="sidebarToggle" href="#">
        <i class="fas fa-bars"></i>
      </button>
      <?php
      require 'php/webPhp/recupererEtat.php';
      $etat = recupererEtat();
      if($etat==0){
        echo('<button type="button" class="btn btn-success" onclick="window.location.href=\'http://thomasfaure05.alwaysdata.net/php/activerProgramme.php\'">Allumer programme</button>');
      }else{
        echo('<button type="button" class="btn btn-danger" onclick="window.location.href=\'http://thomasfaure05.alwaysdata.net/php/desactiverProgramme.php\'">Eteindre programme</button>');

      }
      ?>



      <!-- Navbar -->
      <ul class="navbar-nav ml-auto ml-md-0">



      </ul>

    </nav>