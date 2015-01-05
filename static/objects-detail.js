$(function() {
    function check_time(btn) {
        txt = $("#"+btn.data("target"))
        if (txt.data("viewtimeout") != "0") {
            txt.next().text(" ("+txt.data("viewtimeout") + " sec)")
            txt.data("viewtimeout",txt.data("viewtimeout")-1)
            window.setTimeout(check_time, 1000, btn);
        } else {
            btn.show("slow")
            txt.hide("slow")
            txt.val("")
            txt.next().text("")
            txt.data("viewtimeout",15)
        }
    }
    $(".btn-password").click(function() {
        btn = $(this);
        btn.hide("slow")
        $.post(
            pwd_req_url.replace("0",btn.data("id")),
             { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
             function(data) {
                if (data.password) {
                    txt = $("#"+btn.data("target"))
                    txt.attr("size",data.password.length)
                    txt.val(data.password)
                    txt.data("view-sec", 15)
                    txt.show("slow")
                    window.setTimeout(check_time, 1000, btn);
                } else {
                    alert("Richiesta non riuscita, provare a ricaricare la pagina")
                }
             }
        );
        event.preventDefault()

    });
})