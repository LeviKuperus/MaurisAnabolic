<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>phph</title>
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
        <li><a href="allpurpose.html">Annotationviewer </a></li>
        <li><a href="translator.html">Translator</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </nav>
  </header>
  <div id="hero"><img src="images/starship5D.png" alt="" height="100"/></div>
  <article id="main">
    <h2>Mauris Anabolic test versie</h2>
    <p>Mauris Translator Anabolic is een translator tool voor aminozuren op basis van Python 3. Draaiend achter de ontwikkelingen op de Hogeschool van Arnhem en Nijmegen.</p>
    <p>
  <figure class="centered"></figure>
    </p>
    <figure class="centered">
      <figcaption><a href="#">Start Translator</a></figcaption>
    </figure>
    <?php
	$query = 'mtor'; //your query term
	$dnum = 100; // total number of documents here it's set to 100
	$pids = ''; // PubMED record ID's from e-search initialize to NULL
	$term = 360; // time interval of when documents were published - this one is one year=360days
	
	//retreive PID's of all articles published withing past year that contain query term
	$esearch = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=$query&reldate=$term&datetype=edat&retmax=100&usehistory=y";
	$handle = fopen($esearch, "r");
	$rettype = "abstract"; //retreives abstract of the record, rather than full record
	$retmode = "xml";
	$utils = "http://www.ncbi.nlm.nih.gov/entrez/eutils";
	if (!$handle) {die();}
	
	//collect returned pubmed PID's
	while (!feof ($handle))
	$pids .= fgets($handle, 4096);
	fclose($handle);
	
	//Get query string from eSearch
	preg_match("/(\w+)<\/QueryKey>/i",$pids,$match);
	$queryKey = $match[1];
	
	//get webenv
	preg_match("/(\S+)<\/WebEnv>/i",$pids,$match);
	$webEnv = $match[1];
	$retstart = 0;
	
	//fetch xml docs from PUBMED for returned PID's
	$efetch = "$utils/efetch.fcgi?rettype=$rettype&retmode=$retmode&retstart=$retstart&retmax=$dnum&db=pubmed&query_key=$queryKey&WebEnv=$webEnv&email=abc@xyz.com";
	$pids = '';
	$handle = fopen($efetch, "r");
	if(!$handle) { die(); }
	while (!feof ($handle))
	$pids .= fgets($handle, 4096);
	echo $pids;
	fclose($handle);
	?>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>Patrick Croonen, Levi Kuperus en Louis Voet</p>
  </article>
  <aside id="sidebar">
    <h2>Release notes    </h2>
    <p>Version 0.1a: Eerste versie</p>
  </aside>
  <footer>
    <p>© Copyright Hogeschool van Arnhem Nijmegen Bioinformatica</p>
  </footer>
</div>
</body>
</html>
