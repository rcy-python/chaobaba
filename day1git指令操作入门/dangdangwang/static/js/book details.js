window.onload=function () {
    var buy_num=$('#buy-num');
    var part_buy_button = $('#part_buy_button')
    var buy_now_button = $("#buy_now_button")
    var csrf_token = $('[name="csrfmiddlewaretoken"]').val()
    $('#num_add').click(
        function () {
            buy_num.val(parseInt(buy_num.val())+1)
            $('#num_del').attr('class','num_del')
        }
    )
    $('#num_del').click(
        function () {
            if(parseInt(buy_num.val())===2){
                $('#num_del').attr('class','num_del num_disabled')
                buy_num.val(parseInt(buy_num.val())-1)
            }
            else if(parseInt(buy_num.val()) <= 1){
            }
            else {
                $('#num_del').attr('class','num_del')
                buy_num.val(parseInt(buy_num.val())-1)
            }

        }
    )
    buy_num.blur(
    function () {
       if(parseInt(buy_num.val())>=1){
           $('#num_del').attr('class','num_del')
        }
        else{
            buy_num.val(1)
            $('#num_del').attr('class','num_del num_disabled')
        }
    }
    )

    part_buy_button.click(
        function() {
            console.log(111)
            var id= $('#wodeid').html()
            var buy_numa=$('#buy-num').val()
            $.ajax(
                {
                    type:"POST",
                    url:'/car/add_car/',
                    data:{"id":id,"count1":buy_numa,"csrfmiddlewaretoken":csrf_token},
                   success:function (msg) {
                                if(msg==="未登录添加新购物车"){
                                    alert("未登录添加新购物车")
                                }
                                if(msg==="未登录添加书"){
                                    alert("未登录添加书")
                                }
                                if(msg==="登录中更改旧书"){
                                    alert("登录中:更改旧书")
                                }
                                if(msg==="登录中添加新书"){
                                    alert("登录中:添加新书")
                                }
                }}
            )
        }
    )
    buy_now_button.click(
        function () {
            var id= $('#wodeid').html()
            $.ajax(
                {
                    type:"POST",
                    url:'/car/add_car/',
                    data:{"id":id,"count1":1,"csrfmiddlewaretoken":csrf_token},
                   success:function (msg) {
                                if(msg==="未登录添加新购物车"){
                                    alert("未登录添加新购物车")
                                }
                                if(msg==="未登录添加书"){
                                    alert("未登录添加书")
                                }
                                if(msg==="登录中更改旧书"){
                                    alert("登录中:更改旧书")
                                }
                                if(msg==="登录中添加新书"){
                                    alert("登录中:添加新书")
                                }
                }})
            location.href="/order/address"
        }
    )

}