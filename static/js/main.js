
let width=100;
function increase(){
    document.getElementById("inside").textContent="100%";
    document.getElementById("inside").style.width="100%";
};
function aletrting(){
    window.alert("thank you for subcring");
}
document.addEventListener("DOMContentLoaded",()=>
{
document.getElementById("myImage").src="/static/assets/images/lucos.jpg";
 increase();
});

let btn=document.querySelector("download");
let img=document.querySelector("myImage");
btn.addEventListener("click",()=>
{
    let imagePath=img.getAttribute("src");
    let fileName=getFileName(imagePath);
    saveAs(imagePath,fileName);

});
function getFileName(str){
    return str.subString(str.lastIndexOf('/')+1);
}
