$('.hid').css('display','none')

$(document).ready(function() {
    $(".replybtn").click(function(event){
        event.preventDefault();
        $(this).next(".child_comments").fadeToggle();
    });
});


// document.addEventListener('DOMContentLoaded', function() {
// var enter_btn = document.getElementById('exampleFormControlTextarea1')

// enter_btn.addEventListener('keydown',function(e){
//     if(e.key == "Enter"){
//         e.preventDefault();
//         document.getElementById("devil").click();
//     }
// })

var delete_btn = document.getElementById('delete')

document.body.addEventListener('keyup',function(e){
    e.preventDefault();
    if(e.key == "Enter"){
        console.log("yes")
    document.getElementById('delete').click()
    }
})

