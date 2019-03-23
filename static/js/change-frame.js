// function cross(pk, number){
//     // let cross = document.getElementById('pk');
//     let indicatorId = pk+"-"+number;
//     let cross = document.getElementById(indicatorId);
//     if(cross.className == "pendent-goals"){
//         cross.className = "pendent-goals-cross";
//     }
//     else if(cross.className == "pendent-goals-cross"){
//         cross.className = "pendent-goals";
//     }
// }

function frame(pk, number){
    let indicatorId = pk+"-"+number;
    console.log(indicatorId)
    let frame1 = document.getElementById('year-1');
    let frame2 = document.getElementById('month-2');
    let frame3 = document.getElementById('week-3');
    let frame4 = document.getElementById('day-4');


    if(indicatorId == frame1.id){
        console.log('hfj')
        frame1.className = "performance-subtitle-blue";
        frame2.className = "performance-subtitle";
        frame3.className = "performance-subtitle";
        frame4.className = "performance-subtitle";
    }
    else if(indicatorId === frame2.id){
        frame2.className = "performance-subtitle-blue";
        frame1.className = "performance-subtitle";
        frame3.className = "performance-subtitle";
        frame4.className = "performance-subtitle";
    }
    else if(indicatorId === frame3.id){
        frame3.className = "performance-subtitle-blue";
        frame1.className = "performance-subtitle";
        frame2.className = "performance-subtitle";
        frame4.className = "performance-subtitle";
    }
    else if(indicatorId === frame4.id){
        frame4.className = "performance-subtitle-blue";
        frame1.className = "performance-subtitle";
        frame2.className = "performance-subtitle";
        frame3.className = "performance-subtitle";
    }
}