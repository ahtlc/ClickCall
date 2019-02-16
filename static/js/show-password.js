
function showPassword() {
  var element = document.getElementById("pwd");
  var element2 = document.getElementById("eye");

  if(pwd.value != ""){

    if (pwd.type === "password") {
      pwd.type = "text";
      element2.className = "show2";
      document.getElementById("eye").src= "../../static/img/eye-open.png";
    } else {
      pwd.type = "password";
      element2.className = "show";
      document.getElementById("eye").src= "../../static/img/eyes-closed.png";
    }
  }
}