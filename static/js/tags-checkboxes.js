function changeCheckbox(id, myId){
    var toChange = document.getElementById(id);
    var changeColor = document.getElementById(myId);
    toChange.checked = !toChange.checked;
    if(toChange.checked){
        changeColor.style.backgroundColor = '#27B2FF';
        changeColor.style.color = '#FFFFFF';
    }
    else{
        changeColor.style.backgroundColor= '#DEDEDE';
        changeColor.style.color = '#4D4D4D';
        
    }
} 
function swapCheck(myId, otherId,checkId){
    var activate = document.getElementById(otherId);
    var desactivate = document.getElementById(myId);
    var checkbox = document.getElementById(checkId);
    checkbox.checked = !checkbox.checked;
    activate.style.display = 'flex';
    desactivate.style.display = 'none';
}