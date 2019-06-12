#!python

print("Content-Type: text/html")
print()
import cgi, os

form = cgi.FieldStorage()
#contentsName = form["text1"].value
#styleName = form["text2"].value
print('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="How to create an image upload form without page refresh using Bootstrap, jQuery AJAX and PHP.">
    <meta name="author" content="ShinDarth">

    <title>GAJAH</title>

    <link rel="icon" href="11.png">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">
    <style>body { padding-top:50px; }.navbar-inverse .navbar-nav > li > a { color: #DBE4E1; }</style>

    <!--[if IE]>
      <script src="https://cdn.jsdelivr.net/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://cdn.jsdelivr.net/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">GAJAH</a>
        </div>

        <div class="collapse navbar-collapse">
             <ul class="nav navbar-nav">
             <li class="active"><a href="#">Mixing</a></li>
             <li class="static"><a href = "index.html"> Come Back GAJAH Main</a>  </li>
          </ul>
        </div><!--.nav-collapse -->
      </div>
    </nav>

    <div class="container">

      <!-- Featured Project Row -->
      <div class="row align-items-center no-gutters mb-4 mb-lg-5">
        <div class="mx-auto text-center">
          <img class="img-fluid mb-3 mb-lg-0" src="bg-masthead.jpg" alt="">
        </div>
        <div class="col-xl-4 col-lg-5">
          <div class="featured-text text-center text-lg-left">
            <h4></h4>

          </div>
        </div>
      </div>

      <!-- Header -->
   <header class="masthead">
    <div class="container d-flex h-100 align-items-center">
      <div class="mx-auto text-center">
        <h1 class="mx-auto my-0 text-uppercase"></h1>
        <h2>Image Transfer</h2>
        <h2></h2> Enjoy art however you want !</h2>
        <h2></h2> </h2>

      </div>
    </div>
   </header>



    <div class="container">

      <div style="max-width: 650px; margin: auto;">
        <h1 class="page-header">1.Image Upload</h1>
        <p class="lead">Select Image.</p>

        <form id="upload-image-form" action="" method="post" enctype="multipart/form-data">
          <div id="image-preview-div" style="display: none">
            <label for="exampleInputFile">Selected image:</label>
            <br>
            <img id="preview-img" src="noimage">
          </div>
          <div class="form-group">
            <input type="file" name="file" id="file" required>
          </div>
          <button class="btn btn-lg btn-primary" id="upload-button" type="submit" disabled>Upload image</button>
        </form>

        <br>
        <div class="alert alert-info" id="loading" style="display: none;" role="alert">
          Uploading image...
          <div class="progress">
            <div class="progress-bar progress-bar-striped active" role="progressbar" aria-valuenow="45" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
            </div>
          </div>
        </div>
        <div id="message"></div>
      </div>

      <a target="_blank" href="https://github.com/gksthd1992/gajah"><img style="position: absolute; top: 50px; right: 0; border: 0;" src="https://camo.githubusercontent.com/38ef81f8aca64bb9a64448d0d70f1308ef5341ab/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f6461726b626c75655f3132313632312e706e67" alt="Fork me on GitHub" data-canonical-src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png"></a>

    </div><!--여기거 끝 -->


    </div>

    <div style="max-width: 650px; margin: auto;">
    <a>RGB Color</a>
<P><SCRIPT language="JavaScript">
<!--
var hex = new Array(6)
// assign non-dithered descriptors
hex[0] = "FF"
hex[1] = "CC"
hex[2] = "99"
hex[3] = "66"
hex[4] = "33"
hex[5] = "00"

////////////// 이 drawCell 함수가 레드 그린 블루로 rgb값 받을 수 있는 부분이야!!!!!! 이부분에서 얻는 값으로 파이썬ㅇ[ 활용 할 수 있을것 같아 ㅜㅜ
// draw a single table cell based on all descriptors
function drawCell(red, green, blue) {
    // open cell with specified hexadecimal triplet background color
    document.write('<TD BGCOLOR="#' + red + green + blue + '">')
    // open a hypertext link with javascript: scheme to call display function
    document.write('<A HREF="javascript:display(\'' + (red + green + blue) + '\')">')
    // print transparent image (use any height and width)
    document.write('<IMG SRC="../img/place.gif" BORDER=0 HEIGHT=11 WIDTH=11>')
    // close link tag
    document.write('</A>')
    // close table cell
    document.write('</TD>')
}

// draw table row based on red and blue descriptors
function drawRow(red, blue) {
// open table row
document.write('<TR>')
// loop through all non-dithered color descripters as green hex
for (var i = 0; i < 6; ++i) {
  drawCell(red, hex[i], blue)
}
// close current table row
document.write('</TR>')
}

// draw table for one of six color cube panels
function drawTable(blue) {
// open table (one of six cube panels)
document.write('<TABLE CELLPADDING=0 CELLSPACING=0 BORDER=0>')
// loop through all non-dithered color descripters as red hex
for (var i = 0; i < 6; ++i) {
  drawRow(hex[i], blue)
}
// close current table
document.write('</TABLE>')
}


// draw all cube panels inside table cells
function drawCube() {
// open table
document.write('<TABLE CELLPADDING=5 CELLSPACING=0 BORDER=1><TR>')
// loop through all non-dithered color descripters as blue hex
for (var i = 0; i < 6; ++i) {
  // open table cell with white background color
  document.write('<TD BGCOLOR="#FFFFFF">')
  // call function to create cube panel with hex[i] blue hex
  drawTable(hex[i])
  // close current table cell
  document.write('</TD>')
}
// close table row and table
document.write('</TR></TABLE>')
}

// call function to begin execution
drawCube()
</SCRIPT>
   <div class="container">
        <h1 class="page-header">* RGB Recommand</h1>

        <form action="RGB.py">
            <h1 class="lead">choose image name: </h1>
            <p><input type="text" name="iii" size="20" placeholder = "ex) myFace.jpg ..."></p>

            <p><input type = "submit"></p>
            <p></p>

        </form>


    </div>


    
    <div class="container">
        <form id="upload-image-form" action="" method="post" enctype="multipart/form-data">
          <h1 class="page-header">2. Choose Art</h1>
          <p class="lead">GAJAH Art Default Image</p>
          <p class="lead"></p>
          <div id="image-preview-div" style="display: none">
            <label for="exampleInputFile">Selected image:</label>
            <br>
            <img id="preview-img" src="noimage">
          </div>
          <div class="form-group">
              <p class="lead">==(flower.jpg)=-=-=-=-=-=(woman.jpg)=-=-=-=-=-=(Stary-night.jpg)= </p>
              <input type="image" src ="./a.jpg"  width="200" height="300" type= "summit" >
              <input type="image" src ="./b.jpg" alt = "ff" width="200" height="300" type= "summit" >
              <input type="image" src ="./c.jpg" alt = "Stary-night" width="200" height="300" type= "summit" >
              <p class="lead">=================================================== </p>

          </div>
        </form>
    </div>

    <div class="container">
        <h1 class="page-header">GAJAH Mixing</h1>

        <form action="process_create.py">
            <h1 class="lead">Contents Image: </h1>
            <p><input type="text" name="Contents" size="20" placeholder = "ex) myFace.jpg ..."></p>
            <h1 class="lead">Style Image:</h1>
            <p><input type="text" name="Style" size="20" placeholder = "ex) Ss.jpg ..."></p>
            <p class="lead"> Are you sure? </p>

            <p><input type = "submit"></p>
            <p></p>

        </form>


    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
    <script src="upload-image.js"></script>
  </body>
</html>

''')
