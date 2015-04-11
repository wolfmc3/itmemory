$(function() {
    function copyToClipboard(text) {
      window.prompt("Copy to clipboard: Ctrl+C, Enter", text);
    }
    $(".copyclipboard").click(function(){
        copyToClipboard($(this).parent().next().val());
        event.preventDefault()
    })
    function check_time(btn, next) {
        txt = $("#"+btn.data("target"))
        if (txt.data("viewtimeout") != "0") {
            txt.next().text(txt.data("viewtimeout") + " sec")
            txt.data("viewtimeout",txt.data("viewtimeout")-1)
            if (next) window.setTimeout(check_time, 1000, btn, true);
        } else {
            btn.fadeIn()
            txt.parent().fadeOut()
            txt.val("")
            txt.next().text("...")
            txt.data("viewtimeout",15)
        }
    }

    $(".ajax_get").click(function(event) {
        $('#modalForm .modal-body').load(
            this.href,
            function(){
                $('#modalForm').modal('show');
            });
        event.preventDefault()
    })

    $(".btn-password").click(function() {
        btn = $(this);
        btn.fadeOut()
        $.post(
            pwd_req_url.replace("0",btn.data("id")),
             { 'csrfmiddlewaretoken': csrfmiddlewaretoken },
             function(data) {
                if (data.password) {
                    txt = $("#"+btn.data("target"))
                    txt.val(data.password)
                    txt.data("view-sec", 15)
                    txt.parent().fadeIn()
                    check_time(btn, false)
                    window.setTimeout(check_time, 1000, btn, true);
                } else {
                    alert("Richiesta non riuscita, provare a ricaricare la pagina")
                }
             }
        );
        event.preventDefault()

    });
    var url = document.location.toString();
    if (url.match('#')) {
        $('.nav-tabs a[href=#'+url.split('#')[1]+']').tab('show') ;
    } else {
        $('.nav-tabs a[href=#panel_password]').tab('show') ;
    }

    // Change hash for page-reload
    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
        window.location.hash = e.target.hash;
        window.scrollTo(0, 0)
    })
})