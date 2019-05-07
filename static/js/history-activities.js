function expandHistory(id){
    let toExpand = document.getElementById(id);
    if(toExpand.style.maxHeight=='0px'){
        toExpand.style.maxHeight = '500px';
        toExpand.style.padding = '10px';
    }
    else{
        toExpand.style.maxHeight = '0px';
        toExpand.style.padding = '0px';
    }
} 
