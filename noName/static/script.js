function login(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    var dat = {'username':username, 'password':password};

    $.ajax('/login',{
        method: 'POST',
        data: JSON.stringify(dat),
        dataType: "json",
        contentType: "application/json",
    }).done(function(res){

      if (res['status'] == 'success'){
        $("#stat").html('<b>Successful Login<b>');
      }
      else{
        $("#stat").html('<b>Login Failed</b>');
      }

    }).fail(function(err){
        $("#stat").html(err);
    });
}