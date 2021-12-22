$(document).ready(function() {
    
    
    // add product ajax
    var endpoint = "/add/";

    $('#saveChanges').on('click', function(){
        console.log("form submitted");
        create_post();
    });

    function create_post(){
        console.log("create post is working!");
        product = $('#product_name').val();
        price = $('#product_price').val();
        category = $('#category').val();

        data = {
            "name": product,
            "price": price,
            "category": category
        }
        console.log(data);

        $.ajax({
            url: endpoint,
            type: 'POST',
            // headers: {'X-CSRFToken': getCookie('csrftoken')},
            data: {"data": JSON.stringify(data), 'csrfmiddlewaretoken': $('#btn-csrf').attr('name')},
            success: function(json){
                $("#product_name").val('');
                $("#product_price").val('');
                $("#category").prop("selectedIndex", 0);

                console.log(json);
                console.log('success');
                document.location.reload(true);
            },
            error: function(xhr, errmsg, err){
                console.log(xhr.status + ": " + xhr.responseText);
            }            
        });
    }

    $('#show-btn').click(function(){
        console.log($('#show-btn').attr('data-url'));
        show_data($(this).attr('data-url'));
    });

    function show_data(url){
        console.log(url);
        id = url.replace('/^[0-9]/g', '');
        // id = id.join("")
        console.log(id);
        $.ajax({
            url: url,
            type: 'GET',
            data: {'id': id},
            success: function(json){
                console.log(json)
                $('#prod-name').html(json['name']);
                $('#prod-price').html(json['price']);
                $('#prod-cat').html(json['category']);
                $('#prod-date').html(json['date_created']);
            },
            error: function(xhr, errmsg,err){
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    $('#update').click(function() {
        console.log($(this).attr('data-url'));
        fetch_update_product($(this).attr('data-url'));
    });

    function fetch_update_product(url){
        id = url.replace('/^[0-9]/g', '');
        $.ajax({
            url: url,
            type: 'GET',
            data: {'id': id},
            success: function(json){
                console.log(json);
                $('#update_product_name').val(json['name']);
                $('#update_product_price').val(json['price']);
                $('#update_category').val(json['category']);
            },
            error: function(xhr, errmsg, err){
                console.log(xhr.status + ': ' + xhr.responseText);
            } 
        });
    }

    $('#updateProduct').click(function(){
        product_name = $('#update_product_name').val();
        product_price = $('#update_product_price').val();
        category = $('#update_category').val()

        data = {
            "name": product_name,
            "price": product_price,
            "category": category
        }

        url = $('#update').attr('data-url');
        id = url.replace('/^[0-9]/g', '');

        $.ajax({
            url: url,
            type: 'POST',
            data: {
                'id': id,
                'data': JSON.stringify(data),
                'csrfmiddlewaretoken': $('#update-csrf').attr('name')
            },
            success: function(json){
                console.log(json);
                $('#update_product_name').val('');
                $('#update_product_price').val('');
                $('#update_category').prop('selectedIndex', 0);
                console.log('update success');
                document.location.reload(true);
            },
            error: function(xhr, errmsg, err){
                console.log(xhr.status + ': ' + xhr.responseText);
            }
        });
    });


    $('#delete').click(function() {
        console.log($(this).attr('data-url'));
        fetch_delete_product($(this).attr('data-url'));
    });

    function fetch_delete_product(url){
        // id = url.replace('/^[0-9]/g', '');
        id = $('#delete').attr('get-id');
        console.log(id);
        $.ajax({
            url: url,
            type: 'GET',
            cache: false,
            async:true,
            data: {'id': id},
            success: function(json){
                console.log(json);
                $('#product-name').html(json['name']);
            },
            error: function(xhr, errmsg, err){
                console.log(xhr.status + ": " + xhr.responseText);
            }
        })
    }

    $('#deleteProduct').click(function() {
        url = $('#delete').attr('data-url');
        id = url.replace('/^[0-9/g', '');
        $.ajax({
            url: url,
            type: 'POST',
            dataType: 'json',
            cache: false,
            async: true,
            data: {'id': id, 'csrfmiddlewaretoken': $('#delete-csrf').attr('name')},
            success: function(json){
                console.log(json);
                $('#product-name').html('');
                document.location.reload(true);
            },
            error: function(xhr, errmsg, err){
                console.log(xhr.status + ": " + xhr.responseText);
            }
        })
    });

    function getCookie(c_name)
    {
        if (document.cookie.length > 0)
        {
            c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1)
            {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
    }
});