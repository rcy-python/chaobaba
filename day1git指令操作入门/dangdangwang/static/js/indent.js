window.onload = function () {
    var csrf_token = $('[name="csrfmiddlewaretoken"]').val()
    var name = $("#name")
    var address = $("#address")
    var post_card = $("#post_card")
    var cellphone = $("#cellphone")
    var phone = $("#phone")
    var address_true = 0
    var post_code_true = 0
    var phone_true = 0
    var name_true = 0
    var sumall = $('[name = "sum"]')
    $("#address_id").change(function () {
        var a = $("#address_id option:checked").attr('value')

        if (a === "0") {
            name.removeAttr("readonly")
            address.removeAttr("readonly")
            post_card.removeAttr("readonly")
            cellphone.removeAttr("readonly")
            phone.removeAttr("readonly")
            name.val("")
            address.val("")
            post_card.val("")
            phone.val("")
            cellphone.val("")
        } else {
            $.ajax({
                type: "post",
                url: "/order/ads_select/",
                data: {"id": a, "csrfmiddlewaretoken": csrf_token},
                success: function (msg) {
                    name.val(msg.name)
                    name.attr("readonly", "readonly")
                    address.val(msg.detail)
                    address.attr("readonly", "readonly")
                    post_card.val(msg.post_code)
                    post_card.attr("readonly", "readonly")
                    phone.val(msg.phone)
                    phone.attr("readonly", "readonly")
                    cellphone.val(msg.cellphone)
                    cellphone.attr("readonly", "readonly")

                }
            })
        }
    })
    $("#submit_btn").click(function () {
        var a = $("#address_id option:checked").attr('value')
        var all_price = parseInt($('[name ="xiaoji" ]').eq(1).text())
        if (a === "0") {
            if (/^1[3456789]\d{9}$/.test(cellphone.val()) || /^[23456789][3456789]\d{5}$/.test(phone.val())) {
                phone_true = 1
            }
            if (/.+?(省|市|自治区|自治州|县|区)/.test(address.val())) {
                address_true = 1
            }
            if (/^\d{6}$/.test(post_card.val())) {
                post_code_true = 1
            }
            if (name.val()) {
                name_true = 1
            }
            console.log(phone_true, address_true, post_code_true, name_true)
            if (phone_true && address_true && post_code_true && name_true) {
                var new_id = 0
                $.ajax({
                    type: "post",
                    url: "/order/create_ads/",
                    data: {
                        "name": name.val(),
                        "address": address.val(),
                        "post_code": post_card.val(),
                        "cellphone": cellphone.val(),
                        "phone": phone.val(),
                        "csrfmiddlewaretoken": csrf_token
                    },
                    success:function (msg) {
                        new_id = msg

                         $.ajax({
                            type: "post",
                            url: "/order/get_new/",
                            data: {"csrfmiddlewaretoken": csrf_token, "ads_id": new_id,"all_price":all_price},
                            success: function (msg) {
                                alert('创建订单成功')
                                location.href = "/order/indentok/"

                            }
                        })
                    }



                })


            } else {
                alert("请核对您所填写的地址")
            }

        }
        else {
            $.ajax(
                {
                    type: "post",
                    url: "/order/get_new/",
                    data: {"csrfmiddlewaretoken": csrf_token, "ads_id": a,"all_price":all_price},
                    success: function (msg) {
                        alert("创建订单成功")
                        location.href = "/order/indentok/"
                    }
                }
            )

        }
    })

    function fsum() {
        var sum_all = 0
        sumall.each(function (i) {
            sum_all += Number(sumall.eq(i).text())
            $('[name=xiaoji]').text(sum_all)

        })

    }

    fsum()


}