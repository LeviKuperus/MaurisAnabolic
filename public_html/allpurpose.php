<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Mauris</title>
<link href="styles/main.css" rel="stylesheet" type="text/css">
<!--The following script tag downloads a font from the Adobe Edge Web Fonts server for use within the web page. We recommend that you do not modify it.--><script>var __adobewebfontsappname__="dreamweaver"</script><script src="http://use.edgefonts.net/source-sans-pro:n6:default.js" type="text/javascript"></script>
</head>

<body>
<div id="wrapper">
  <header id="top">
    <h1>Mauris Anabolic</h1>
    <nav id="mainnav">
      <ul>
        <li><a href="index.html" class="thispage">Home</a></li>
        <li><a href="webapplicatie.html">Webapplication</a></li>
        <li><a href="allpurpose.html">all-purpose tools </a></li>
        <li><a href="translator.html">Translator</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>
  <div id="hero"><img src="images/starship5D.png" alt="" height="100"/></div>
  <article id="main">
    <h2>All-Purpose Tools test versie</h2>
    <p>
    <?php
	print "Dit is een test print op regel 1."
    ?>
    &nbsp;</p>
  </article>
  <aside id="sidebar">
    <h2>Handmatig zoeken in PubMed  </h2>
    <p>
         <input id="ZoekOpdracht" type="text">
	<button type="button" onclick="myFunction()">Zoeken</button>
	<img src="images/faviPubMed.ico" alt=""/>
    <p id="Wait"></p>
<script>
function myFunction() {
    //Get the value of input field with id="numb"
    var val = document.getElementById("ZoekOpdracht").value;

    //Get the element with id="demo"
	var goUrl = "http://www.ncbi.nlm.nih.gov/pubmed/?term="+val;
	window.open(goUrl);
}
</script>
    &nbsp;</p>
  </aside>
  <footer>
    <p>© Copyright Hogeschool van Arnhem Nijmegen Bioinformatica</p>
  </footer>
</div>
</body>
</html>
