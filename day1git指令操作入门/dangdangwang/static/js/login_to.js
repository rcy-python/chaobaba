$('[name="login_to"]').click(function () {
    var a=window.location.href
    $(this).attr("href","/user/login/?url="+a)
})