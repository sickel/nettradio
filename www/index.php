<html><head><title>Nettradio</title>
<script type="text/javascript" src="radio.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1"></head>

<body><br />

<?php

$file='ch.txt';
$file2='ch2.txt';
//print_r($_GET);
$chs=array(
'p1'=>array('NRK P1','http://lyd.nrk.no/nrk_radio_p1_ostlandssendingen_mp3_h'),
'p2'=>array('NRK P2','http://lyd.nrk.no/nrk_radio_p2_mp3_h'),
'p3'=>array('NRK P3','http://lyd.nrk.no/nrk_radio_p3_mp3_h'),
'p13'=>array('NRK P13','http://lyd.nrk.no/nrk_radio_p13_mp3_h'),
'p1pluss'=>array('NRK P1+','http://lyd.nrk.no/nrk_radio_p1pluss_mp3_h'),
'jazz'=>array('NRK alltid jazz','http://lyd.nrk.no/nrk_radio_jazz_mp3_h'),
'klassisk'=>array('NRK alltid klassisk','http://lyd.nrk.no/nrk_radio_klassisk_mp3_h'),
'nyheter'=>array('NRK alltid nyheter','http://lyd.nrk.no/nrk_radio_alltid_nyheter_mp3_h'),
'mp3'=>array('NRK mp3','http://lyd.nrk.no/nrk_radio_mp3_mp3_h')
);
$ch='';
if(array_key_exists('ch',$_GET)){
    $ch=$_GET['ch'];
}else{
   $f=fopen($file,"r");
   if($f){
     $ch=fread($f,filesize($file));
     fclose($f);
  //   print("ch:$ch<-");
   }
   //print("ch ok|$ch|<br/>");
   if(array_key_exists('browse',$_GET)){
    //echo('browse');
      $keys=array_keys($chs);
      //print_r($keys);
      $idx=array_search($ch,$keys);
      //print($idx);
      if($idx===false){
        $ch=$keys[0];
     }else{
        if($_GET['browse']=='prev'){
            $idx--;
        }else{
            $idx++;
        }
        $n=count($keys);
        if ($idx<0){$idx=$n-1;}
        elseif($idx >=$n){
            $idx=0;
            }
        $ch=$keys[$idx];
        //echo($ch);
     }
   }
}
//echo($ch);
if(array_key_exists($ch,$chs)){
  $stream=$chs[$ch][1];
  `/usr/local/bin/radio.sh $stream`;
  $f=fopen($file,"w");
  fwrite($f,$ch);
  fclose($f);
  $f=fopen($file2,"w");
  fwrite($f,$chs[$ch][0]." ");
  fclose($f);
}
if(array_key_exists('off',$_GET) && $_GET['off']=='Av'){
	`/usr/local/bin/radio.sh off`;	
}
?>
<form action="" method="get">
<select name="ch">
<?php
foreach($chs as $k=>$v){
    $sel="";
    if($k==$ch){
        $sel="selected";
    }
    print("<option $sel value=\"{$k}\">{$v[0]}</option>\n");
}
?>
</select>
<input type="submit" value="Velg" />
<input name="off" type="submit" value="Av" />
</form>

<a href="?browse=prev">Forrige</a> 
<a href="?browse=next">Neste</a>  
<p id="radiotext"> </p>
</body></html>

