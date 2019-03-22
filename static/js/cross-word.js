function cross(pk, number){
    // let cross = document.getElementById('pk');
    let indicatorId = pk+"-"+number;
    let cross = document.getElementById(indicatorId);
    if(cross.className == "pendent-goals"){
        cross.className = "pendent-goals-cross";
    }
    else if(cross.className == "pendent-goals-cross"){
        cross.className = "pendent-goals";
    }
}
