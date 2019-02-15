function changeIndicator(indicatorType, pk){
    let indicatorId = indicatorType+"-"+pk;
    let indicator = document.getElementById(indicatorId);


    if(indicator.classList.contains("has-indicator")){
        indicator.classList.remove("has-indicator");
    }
    else{
        indicator.classList.add("has-indicator");
    }
}