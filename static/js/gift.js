var snow_img = "/static/img/gift.png";
//snow_img = document.createElement('img');
//snow_img.src = "/static/img/gift.png";

var leftImg = document.createElement('img');

leftImg.src = ("/static/img/gift.png");

leftImg.style = "position:fixed;left:500px;top:200px;width:64;height:64;z-index:100"
var quest_1_text = $('#quest_1')
var quest_2_text = $('#quest_2')


leftImg.onclick = function() {
    $.ajax({
        type: "GET",
        url: "/quest",
        data: {
        },
        success: function(response) {
        quest_1_text.prop('hidden', true)
            quest_2_text.prop('hidden', false)
            leftImg.prop('hidden', true) // найти как скрыть картинку
        },

        error: function(response){
            console.log(response);

        }



    });

};
document.querySelector('body').appendChild(leftImg);


snow_no = 56;
var timeszimaon = 1;
if (typeof(window.pageYOffset) == "number") {
snow_browser_width = window.innerWidth;
snow_browser_height = window.innerHeight; }
else if (document.body && (document.body.scrollLeft || document.body.scrollTop)) {
snow_browser_width = document.body.offsetWidth;
snow_browser_height = document.body.offsetHeight; }
else if (document.documentElement && (document.documentElement.scrollLeft || document.documentElement.scrollTop)) {
snow_browser_width = document.documentElement.offsetWidth;
snow_browser_height = document.documentElement.offsetHeight; }
else {
snow_browser_width = 500;
snow_browser_height = 500; }
snow_dx = [];
snow_xp = [];
snow_yp = [];
snow_am = [];
snow_stx = [];
snow_sty = [];
if (timeszimaon == 1) {
for (i = 0; i < snow_no; i++) {
snow_dx[i] = 0;
snow_xp[i] = Math.random()*(snow_browser_width-50);
snow_yp[i] = Math.random()*snow_browser_height;
snow_am[i] = Math.random()*20;
snow_stx[i] = 0.02 + Math.random()/10;
snow_sty[i] = 0.7 + Math.random();
//����� �������� ������� �������� �� ���� z-index
if (i == 0) document.write("<\div id=\"snow_flake0\" style=\"position:absolute;z-index:0\"><a href=\"#\" target=\"_blank\"><\img src=\""+snow_img+"\" border=\"0\"></a><\/div>");
else document.write("<\div id=\"snow_flake"+ i +"\" style=\"position:absolute;z-index:10000"+i+"\"><\img src=\""+snow_img+"\" border=\"0\"><\/div>");
}
}
function SnowStart() {
for (i = 0; i < snow_no; i++) {
snow_yp[i] += snow_sty[i];
if (snow_yp[i] > snow_browser_height-50) {
snow_xp[i] = Math.random()*(snow_browser_width-snow_am[i]-30);
snow_yp[i] = 0;
snow_stx[i] = 0.02 + Math.random()/10;
snow_sty[i] = 0.9 + Math.random();}
snow_dx[i] += snow_stx[i];
document.getElementById("snow_flake"+i).style.top=snow_yp[i]+"px";
document.getElementById("snow_flake"+i).style.left=snow_xp[i] + snow_am[i]*Math.sin(snow_dx[i])+"px";}
snow_time = setTimeout("SnowStart()", 10); }
if (timeszimaon == 1) { SnowStart(); }