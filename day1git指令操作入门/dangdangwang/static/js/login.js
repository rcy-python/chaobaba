window.onload=function(){
    //验证码
     $('#vcodeImgBtn1').click(function () {
    var url = '/user/get_captcha/?'+(new Date()).getTime()
    $('#imgVcode1').attr('src',url)
    $('#txt_vcode').val(null)
})
     $('#imgVcode1').click(function () {
        var url = '/user/get_captcha/?'+(new Date()).getTime()
        $('#imgVcode1').attr('src',url)
         $('#txt_vcode').val(null)
    })
    //注册
    var al = 0
    var name = $('#txtUsername')
    var password = $('#txtPassword')
     var submitLoginBtn = $('#submitLoginBtn')
    var vcode=$('#txt_vcode')
    var cool = 400
    var url = $("#url").text()
    var csrf_token = $('[name="csrfmiddlewaretoken"]').val()
   name.focus(function () {
        $('#J_tipVcode').attr('style', 'display:none')
       if(!name.val())
        {$('#liDivErrorMessage').text('请输入邮箱/昵称/手机号码')}
      $('#liDivErrorMessage').attr('style','display:inline-block;')
    })
    name.blur(function () {
        if(!name.val())
        {$('#liDivErrorMessage').attr('style','display:none')}
        else {
            $.ajax(
            {
                type:'post',
                data:{"csrfmiddlewaretoken":csrf_token,"name":name.val()},
                url:'/user/ajax_name/',
                success: function (msg) {
                    if (msg === "true") {
                        console.log(1);
                        $('#liDivErrorMessage').attr('style', 'display:inline-block;color:red')
                        $('#liDivErrorMessage').html('此账号未注册，&nbsp;<a href="/user/register/" name="mobile_login _link" class="more">立即注册</a>')
                        cool = 300
                    }
                    else {
                        $('#liDivErrorMessage').attr('style', 'display:inline-block;color:green')
                        $('#liDivErrorMessage').text('该账号已注册,可以登陆')
                        cool = 200
                    }
                }}
        )}

    })
    password.focus(function () {
        $('#J_tipVcode').attr('style', 'display:none')
        $('#login_password_error').attr('style','display:inline-block')
    })
    password.blur(function () {
        $('#login_password_error').attr('style','display:none')
    })
     var autologin = $('#autologin')
    autologin.click(function () {
        if(autologin.is(':checked')){
            $("#auto_sure" ).text('请勿在公用电脑上勾选此选项')
            al = 1
        }
        else {
             $("#auto_sure" ).text('七天内自动登录')
            al = 0
        }

    })
    submitLoginBtn.click(function(){
        if(!name.val()){
            alert('用户名不能为空')
        }
        else if(!password.val()){
            alert('密码不能为空')
        }
        else if(!vcode.val()){
            alert('验证码不能为空')
        }
        else if(cool!==200){
            alert('用户名未注册或已失效')
        }
        else {
            $.ajax(
                {
                    type:'POST',
                    url:'/user/login_result/',
                    data:{"csrfmiddlewaretoken":csrf_token,"name":name.val(),"password":password.val(),"vcode":vcode.val(),'auto':al},
                    success:function (msg) {
                        if (msg === 'code_error') {
                            $('#J_tipVcode').attr('style', 'display:inline-block;color:red')
                        } else {
                            if (msg === 'password_error') {
                               $('#liDivErrorMessage').attr('style', 'display:inline-block;color:red')
                                $('#liDivErrorMessage').text('账号或密码错误')
                            }

                         else {
                            alert('登录成功')
                            location.href = url
                        }}


                    }
                }
            )
        }
    })
   }
