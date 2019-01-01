<html><head><title>Nettradio</title>
<script type="text/javascript" src="radio.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1"></head>
<body><br />
<?php
$file='ch.txt'; 
$file2='ch2.txt';
$chs=array();
# Reading in stations from file:
$file = fopen("stationlist.txt", "r") or exit("Unable to open file!");
while(!feof($file))
  {
    $line=fgets($file);
    $list=explode(",",$line);
    if(count($line)==3 && $list[0]){
        $chs[$list[0]]=[$list[1],$list[2]];}
  }
fclose($file);

$ch='';
if(array_key_exists('ch',$_GET)){
    $ch=$_GET['ch'];
}else{
   $f=fopen($file,"r");
   if($f){
     $ch=fread($f,filesize($file));
     fclose($f);
   }
   if(array_key_exists('browse',$_GET)){
      $keys=array_keys($chs);
      $idx=array_search($ch,$keys);
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
     }
   }
}

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
<select name="ch" id ="chselector">
<?php
foreach($chs as $k=>$v){
    $sel="";
    if($k==$ch){
        $sel='selected="selected"';
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
<p>
Volum: <span id="volumevalue">0</span>% <button id="down" class="volbutton">-</button><button id="up" class="volbutton">+</button>
</p>
<p id="radiotext"> </p>
</body></html>
