window.onload=function(){
    numberesult()
        xiaoji()
var csrf_token = $('[name="csrfmiddlewaretoken"]').val()
    $("[name = 'add_num']").click(function () {
         var id =$(this).parent().next().text()
         var a = $(this).parent().parent().prev()
         var b = $(this).parent().parent().next()
        $(this).prev().val(parseInt($(this).prev().val())+1)
        numberesult()
        xiaoji()
        $.ajax({
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
                                if(msg==="登录中添加旧书"){
                                    alert("登录中:添加旧书")
                                }
                                if(msg==="登录中添加新书"){
                                    alert("登录中:添加新书")
                                }


            }
        })
    })
    $("[name = 'sub_num']").click(function () {

        var id =$(this).parent().next().text()
        if (parseInt($(this).next().val())<=1){
            $(this).next().val(1)
            alert("只剩一本书啦~")
        }
        else{
            $(this).next().val(parseInt($(this).next().val())-1)
            numberesult()
            xiaoji()
            $.ajax({
             type:"POST",
                    url:'/car/add_car/',
                    data:{"id":id,"count1":-1,"csrfmiddlewaretoken":csrf_token},
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

            }
        })
        }


    })
    $("[name = 'delete']").click(function(){
            var id = $(this).parent().next().text()
            var mymessage=confirm("确认删除吗？");
             if(mymessage===true){
                 $(this).parent().parent().parent().remove()
            numberesult()
            xiaoji()
            $.ajax({
             type:"POST",
                    url:'/car/rem_car/',
                    data:{"id":id,"csrfmiddlewaretoken":csrf_token},
                    success:function (msg) {
                        if(msg==="从数据库删除成功"){
                            alert("从数据库删除成功")
                                }
                        if(msg==="从session删除成功"){
                            alert("从session删除成功")
                                }
                        if(msg==="删光了"){
                            location.href=''
                                }

            }
        })
             }
             else{}
        })
    $("[name = 'vall']").blur(
        function () {
            var id =$(this).parent().next().text()
            console.log(id)
            console.log($(this).val());
            if(parseInt($(this).val())>=1){}
            else {$(this).val(1)}
            var count1 = $(this).val()
            console.log(count1)
             $.ajax({
             type:"POST",
                    url:'/car/update_car/',
                    data:{"id":id,"count1":count1,"csrfmiddlewaretoken":csrf_token},
                    success:function (msg) {
                        if(msg==="从数据库更改成功"){
                            alert("从数据库更改成功")
                                }
                        if(msg==="从session更改成功"){
                            alert("从session更改成功")
                                }
                }

        })
            numberesult()
            xiaoji()
        }
    )
    $("#j_removeproducts").click(function () {
        var mymessage=confirm("确认删除所有商品吗？");
             if(mymessage===true){
                 $.ajax({
             type:"POST",
                    url:'/car/delete_all/',
                    data:{"csrfmiddlewaretoken":csrf_token},
                    success:function (msg) {
                                if(msg==="从数据库删除所有数据"){
                                    location.href=''
                                }
                                if(msg==="删除session所有数据"){
                                    location.href=''
                                }


            }
        })

    }})
    //商品总数:
   function numberesult() {
            var sumnum= $("input[name='vall']");
            var sumall = 0
            sumnum.each(function(i){
                sumall += parseInt(sumnum.eq(i).val())
});
            var element = $("#numall")
            element.text(sumall);
        }
    //小计&总价
    function xiaoji() {
            var sumnum= $("[name='vall']");
             var sumn = 0
            sumnum.each(function(i){
                var one_price = sumnum.eq(i).parent().parent().prev().children().text()
                var all_price = sumnum.eq(i).parent().parent().next().children()
                all_price.text(parseInt(one_price)*parseInt(sumnum.eq(i).val()))
                sumn+=(parseInt(one_price)*parseInt(sumnum.eq(i).val()))
});
            var element = $("#allprice")
            element.text("¥"+sumn+".00");
            var pay = $("#payAmount")
            pay.text("¥"+sumn+".00")  }

    $("#checkout_btn").click(function () {
        window.location.href="/order/address/"
    })
}