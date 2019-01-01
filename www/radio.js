strURL="radiotext.php";


xmlhttpPost(strURL);

var intervalID = setInterval(function(){xmlhttpPost(strURL);}, 5000);

window.onload = function(e) {
    document.getElementById("down").addEventListener("click", changevolume);
    document.getElementById("up").addEventListener("click", changevolume);
} 

function xmlhttpPost(strURL) {
    var xmlHttpReq = false;
    var self = this;
    self.xmlHttpReq = new XMLHttpRequest();
    self.xmlHttpReq.open('POST', strURL, true);
    self.xmlHttpReq.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    self.xmlHttpReq.onreadystatechange = function() {
        if (self.xmlHttpReq.readyState == 4) {
            var ret = JSON.parse(self.xmlHttpReq.responseText);         
            updatepage(ret.text);
            updatedropdown(ret.ch);
            updatevolume(ret.vol);
        }
    }
    self.xmlHttpReq.send();
}

function updatevolume(str){
    document.getElementById("volumevalue").innerHTML = str;
}

function updatepage(str){
    document.getElementById("radiotext").innerHTML = str;
}


function updatedropdown(str){
   var element = document.getElementById('chselector');
   element.value = str;
}

function changevolume(){
    adjust=this.id;
    url="volume.php?adjust="+adjust;
    var self = this;
    self.xmlHttpReq = new XMLHttpRequest();
    self.xmlHttpReq.open('GET', url, true);
    self.xmlHttpReq.send();
}
