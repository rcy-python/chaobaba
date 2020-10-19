window.onload=function () {
//++++++++++++++++++++++++验证码显示++++++++++++++++++++
    $('#imgVcode').click(function () {
        var url = '/user/get_captcha/?'+(new Date()).getTime()
        $('#imgVcode').attr('src',url)
         $('#txt_vcode').val(null)
        ajax_code()
    });
    $('#vcodeImgBtn').click(function () {
        var url = '/user/get_captcha/?'+(new Date()).getTime()
        $('#imgVcode').attr('src',url)
        $('#txt_vcode').val(null)
        ajax_code()
    });
//++++++++++++++++++++++++登录判断++++++++++++++++++
   var name =$("#txt_username");
   var password = $('#txt_password');
   var rpassword = $('#txt_repassword');
   var vcode = $('#txt_vcode')
   var J_tipPassword = $('#J_tipPassword');
   var spn_repassword_ok=$('#spn_repassword_ok');
   var chb_agreement=$('#chb_agreement');
   var J_submitRegister=$('#J_submitRegister')
    var csrf_token = $('[name="csrfmiddlewaretoken"]').val()
    var url = $("#url").text()
    var name_sure = false
    var psw_sure = false
    var rpsw_sure = false
    var code_sure = false
    var a_sure = false
 function rpassword_true() {
         var p = $('#txt_password');
         var r = $('#txt_repassword');
        if(r.val()===p.val()){
           spn_repassword_ok.attr('class','icon_yes');
           spn_repassword_ok.attr('style','display:inline-block')
            rpsw_sure=true
       }
       else {
           spn_repassword_ok.attr('class','icon_wrong');
           spn_repassword_ok.attr('style','display:inline-block')
            rpsw_sure=false
       }
        if (!r.val()){
             spn_repassword_ok.attr('style','display:none')
         }
     }
 function name_true(){
       var spn_username_ok = $('#spn_username_ok');
        if(/^1[3456789]\d{9}$/.test(name.val())||/^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/.test(name.val())){
            $.ajax({
                type:"POST",
                url: "/user/ajax_name/",
                data:{"csrfmiddlewaretoken":csrf_token,"name":name.val()},
                success:function (msg) {
                    if (msg==="true"){
                           spn_username_ok.attr('class','icon_yes');
                           spn_username_ok.attr('style','display:inline-block')
                         $('#J_tipUsername').attr('style','display:none')
                        name_sure=true
                    }
                    else {
                     spn_username_ok.attr('class','icon_wrong');
                     spn_username_ok.attr('style','display:inline-block')
                     $('#J_tipUsername').attr('style','display:inline-block')
                        name_sure=false
                    }
                }
            })
            }
        else {
            spn_username_ok.attr('class','icon_wrong');
            spn_username_ok.attr('style','inline-block')
            $('#J_tipUsername').attr('style','display:none')
            name_sure=false
        }
 }
 function password_true(){
             if (password.val().length<6) {
                J_tipPassword.attr('style', 'display:inline-block');
                $('#spnPwdStrong1').attr('style','display:none');
                $('#spnPwdStrong2').attr('style','display:none');
                $('#spnPwdStrong3').attr('style','display:none');
                $('#spn_password_ok').attr('class', 'icon_wrong')
                $('#spn_password_ok').attr('style', 'display:inline-block')
                 psw_sure=false
       }
         else {psw_sure=true
                 $('#spn_password_ok').attr('class', 'icon_yes')
             $('#spn_password_ok').attr('style', 'display:inline-block');
             J_tipPassword.attr('style', 'display:none');
            if(/^(?=.*\d)(?=.*[a-zA-Z])(?=.*[~!@#$%^&*])[\da-zA-Z~!@#$%^&*]{6,}$/.test(password.val())){
                $('#spnPwdStrong1').attr('style','display:none');
                $('#spnPwdStrong2').attr('style','display:none');
                $('#spnPwdStrong3').attr('style','display:inline-block')
            }
            else if(/(?!^(\d+|[a-zA-Z]+|[~!@#$%^&*?]+)$)^[\w~!@#$%^&*?]/.test(password.val())){
                $('#spnPwdStrong1').attr('style','display:none');
                $('#spnPwdStrong2').attr('style','display:inline-block');
                $('#spnPwdStrong3').attr('style','display:none')
            }
            else if(/^(?:\d+|[a-zA-Z]+|[!@#$%^&*]+)$/.test(password.val())){
                $('#spnPwdStrong1').attr('style','display:inline-block');
                $('#spnPwdStrong2').attr('style','display:none');
                $('#spnPwdStrong3').attr('style','display:none')
            }}
         }
 function ajax_code(){
        $.ajax(
                {
                    type:"POST",
                    url:"/user/ajax_vcode/",
                    data:{"csrfmiddlewaretoken":csrf_token,"code":vcode.val()},
                    success:function(msg) {
                        if(msg==='true') {code_sure=true
                            $('#spn_vcode_ok').attr("style", "display:inline-block")
                            $('#J_tipVcode2').attr("style", "display:none")
                            $('#J_tipVcode').attr("style", "display:none")
                        }
                        else{code_sure=false
                            $('#J_tipVcode2').attr("style","display:inline-block")
                             $('#spn_vcode_ok').attr("style","display:none")
                              $('#J_tipVcode').attr("style","display:inline-block")
                            }
                        }

                }
            )
     if (!vcode.val()){
           code_sure=false
            $('#spn_vcode_ok').attr("style", "display:none")
           $('#J_tipVcode2').attr("style", "display:none")
           $('#J_tipVcode').attr("style", "display:none")
       }
         }
//++++++++++++++++++++++++用户名判断++++++++++++++++++
 name.keyup(function () {
    name_true()
 })
   //++++++++++++++++++++++++密码判断++++++++++++++++++
   password.keyup(function () {
       if(password.val()!==null){
           password_true()
           rpassword_true()
       }
   });
   //++++++++++++++++++++++++重复输入密码判断++++++++++++++++++
   rpassword.keyup(function () {
        if(rpassword.val()!==null){
           rpassword_true()
       }
   })
    rpassword.blur(function () {
        if(rpassword===null){
            spn_repassword_ok.attr('style','display:none')
        }
   })
   vcode.keyup(function () {
   ajax_code()
       if (!vcode.val()){
           code_sure=false
            $('#spn_vcode_ok').attr("style", "display:none")
           $('#J_tipVcode2').attr("style", "display:none")
           $('#J_tipVcode').attr("style", "display:none")
       }
   })

   J_submitRegister.click(
       function () {
           if (chb_agreement.is(':checked')){
               a_sure=true
           }
           else {
               alert("勾选同意后才能进行注册")
               return false
           }
           rpassword_true()
           name_true()
           password_true()
           ajax_code()

           if(!(a_sure&&name_sure&&psw_sure&&rpsw_sure&&code_sure)){
               alert("请核对您所填写的信息")
           }
           else {
               $.ajax({
                    type:"post",
                    url:"/user/register_result/",
                    data:{"csrfmiddlewaretoken":csrf_token,"name":name.val(),"password":password.val()},
                    success:function (msg) {
                        if (msg==="false"){
                            alert('服务器繁忙,请稍候再试')
                        }
                        else {
                            location.href='/user/registerok/?name='+name.val()
                        }
                    }


               })
           }


       }
   )

}
