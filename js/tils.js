
window.onresize = resizeWindow;

window.onload = function () {
  console.log("onload");
  var humberger = document.getElementById("humbergericon");
  humberger.onclick = sideMenu;
}

function resizeWindow(){
  if (window.innerWidth >= 768) 
  {
    sidemenu.style.left = "5px";
  }
  else
  {
    sidemenu.style.left = "-100%";
  }
}

function sideMenu() {
  if(sidemenu.style.left== "5px")
  {
    sidemenu.style.left = "-100%";
  }
  else
  {
    sidemenu.style.left = "5px";
  }
}



//jQuery

/*
$(function(){
  $(".menu").click(function()
  {
    if(sidemenu.style.left== "5px")
    {
      sidemenu.style.left = "-100%";
    }
    else
    {
      sidemenu.style.left = "5px";
    }
  });

  $(window).resize(function()
  {
    if ($(window).width() >= 768) 
    {
      sidemenu.style.left = "5px";
    }
    else
    {
      sidemenu.style.left = "-100%";
    }
  });
});
    */