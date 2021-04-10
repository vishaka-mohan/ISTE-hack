/**Loader */
jQuery(document).ready(function() {
    jQuery("#loader").remove();
});


/*Accordion Functionality*/
let accords=$('.chevron-down')
$.each(accords, function(key, val){
    $(val).click(function(){
        $(val).parent().siblings('.accord-expand').toggleClass('hide')
        let child=$(val).children('.fas');
        if($(child).hasClass('fa-chevron-down')){
            $(child).removeClass('fa-chevron-down')
            $(child).addClass('fa-chevron-up')
        }
        else{
            $(child).removeClass('fa-chevron-up')
            $(child).addClass('fa-chevron-down')
        }
    })
})

let hideAnswers=$('.question-expand');
$.each(hideAnswers, function(key, val){
    $(val).click(function(){
        /*Change Hide answer/ Answer text*/
        if($(val).hasClass('expanded'))
        {
            $(val).removeClass('expanded');
            $(val).text('Answer')
        }
        else{
            $(val).addClass('expanded');
            $(val).text('Hide Answer')
        }

        /*Toggle Answer display*/
        let answer=$(val).parent().next('.answer')
        $(answer).toggleClass('hide');
    })
})