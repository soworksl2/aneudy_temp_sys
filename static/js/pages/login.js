let login_token_input = document.getElementById('login-token');
let login_btn = document.getElementById('login-btn');


function login_btn_click(){
    login_btn.disabled = true;
    login_token_input.disabled = true;

    let token_validity = check_token_validity();

    if (token_validity.validity){
    }else{
        alert(token_validity.msg);
    }

    login_btn.disabled = false
    login_token_input.disabled = false

}
login_btn.addEventListener('click', login_btn_click);


class TokenValidityResponse{
    constructor(validity, msg=''){
        this.validity = validity;
        this.msg = msg;
    }

    static success(){
        return new TokenValidityResponse(true);
    }

    static fail(msg){
        return new TokenValidityResponse(false, msg);
    }
}


function get_token_input(){
    return login_token_input.value.toUpperCase();
}

function is_valid_token(token){
    parts = token.split('-');
    parts = parts.map((e) => e.trim());

    if (parts.length < 2){
        return false;
    }

    if (!parts.every((e) => e.length == 4)){
        return false;
    }

    return true;
}

function check_token_validity(){
    let token = get_token_input();

    if (!is_valid_token(token)) {
        return TokenValidityResponse.fail('el token no es valido');
    }

    return TokenValidityResponse.success();
}
