$(function() {
    $('table tr td[scope="row"]').each(function(index, td) {
        tdObj = $(td);
        url = tdObj.children("a").attr("href");
        tr = $(tdObj.parent());
        tdObj.remove();
        tr.attr("href",url);
        tr.click(function() {
            document.location.href = $(this).attr("href")
        });
        tr.css("cursor","pointer");
        tr.hover(
            function() {
                $(this).addClass("active")
            },
            function() {
                $(this).removeClass("active")
            }
        )
    })
})
