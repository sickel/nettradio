<html><head><title>Nettradio</title>
<script type="text/javascript" src="radio.js"></script>
<meta name="viewport" content="width=device-width, initial-scale=1"></head>
<style>
body {
  background-color: #CCCCCC;
}
#radiotext{
  padding: 10px;
  font-family: sans-serif;
  background-color: #FFFFFF;
  max-width: 300px;
  min-height: 44px;
  font-size: 12px;
}

</style>
<body>
<?php
$chs=array();
# Reading in stations from file:
$file = fopen("stationlist.txt", "r") or exit("Unable to open file!");
while(!feof($file))
  {
    $line=fgets($file);
    if (str_contains($line,',')){
      $list=explode(",",$line);
    
      if($list[1]>""){
        $chs[$list[0]]=[$list[1],$list[2]];}
    }
  }

fclose($file);
$file='ch.txt'; 
$ch='';

# Need to check afterwards if the radio already is running - handling of browsing and off
$running=file_exists('/tmp/radiopid');
unset($_GET['ch']);


if(array_key_exists('ch',$_POST) and !(array_key_exists('browse',$_POST))){
    $ch=$_POST['ch'];
}else{
# if no channels sent in, check if one has been active:   
   $f=fopen($file,"r");
   if($f){
     $ch=fread($f,filesize($file));
     fclose($f);
   }
   if(array_key_exists('browse',$_REQUEST) && $running){
      $keys=array_keys($chs);
      $idx=array_search($ch,$keys);
      if($idx===false){
        $ch=$keys[0];
     }else{
        if($_REQUEST['browse']=='prev'){
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

unset($_GET['ch']); # Should not be used
// $turnoff=(array_key_exists('off',$_REQUEST) && $_REQUEST['off']=='Av');
if(array_key_exists('off',$_GET) and $_GET['off']=='Av'){
  unset($_GET['off']);
}


if(count($_POST) + count($_GET) > 0 and array_key_exists($ch,$chs)){
  $stream=$chs[$ch][1];
  shell_exec(sprintf('%s > /dev/null 2>&1 &',  "/usr/local/bin/radio.sh $stream"));
  $f=fopen($file,"w");
  fwrite($f,$ch);
  fclose($f);
}
if(array_key_exists('off',$_POST) && ($_POST['off']=='Av' || ($_POST['off']=='Toggle' && $running))) {
	`/usr/local/bin/radio.sh off`;	
}
if(array_key_exists('off',$_GET) && ($_GET['off']=='Toggle' && $running)) {
	`/usr/local/bin/radio.sh off`;	
}



?>
<form action="" method="post">
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
<input name="off" type="submit" value="Av" /><button id="popout">&#8599;</button><br />
</form><form method="post">
<button name="browse" value="prev">&lt;--</button>
<button name="browse" value="next">--&gt;</button>
</form>

Volum: <span id="volumevalue">0</span>% <button id="down" class="volbutton">-</button><button id="up" class="volbutton">+</button>
</p>
<p id="radiotext"> </p>
</body></html>
