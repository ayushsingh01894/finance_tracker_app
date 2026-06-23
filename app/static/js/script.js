document.addEventListener("DOMContentLoaded",function(){

console.log("Finance Tracker Loaded")

highlightNav()

})

function highlightNav(){

const links=document.querySelectorAll(".nav-links a")

links.forEach(link=>{

if(link.href===window.location.href){

link.style.fontWeight="bold"

}

})

}