// everything gets mapped in this opening function
$(document).ready(function(){

    $("#colourchange").click(function() {
        $("h1").toggleClass("change_title")

    });

    $("#darkmode").click(function() {
        $(".content").toggleClass("dark-mode")

    });

    $("#hidetext").click(function() {
        $("p").toggle();

    });


});
