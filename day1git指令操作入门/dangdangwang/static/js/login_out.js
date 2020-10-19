$(function () {
    $('#login_out').click(function () {
        var csrf_token = $('[name="csrfmiddlewaretoken"]').val()
        $.ajax({
            type: 'POST',
            url: '/user/login_out/',
            data: {"csrfmiddlewaretoken": csrf_token},
            success: function (msg) {
                if (msg === 'ok') {
                    location.href = ''
                }
            }
        })

    })
})