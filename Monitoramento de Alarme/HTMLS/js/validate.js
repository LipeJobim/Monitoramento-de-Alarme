function validarLogin() {
    var usuario = "root";
    var senha = "root"
    // Obter os valores do usuário e senha
    var usuario = document.getElementById("nome").value;
    var senha = document.getElementById("senha").value;

    // Verificar se o usuário e a senha são válidos
    if (usuario === "root" && senha === "root") {
        alert("Login bem-sucedido! Redirecionando para o sistema...");
        // Aqui você pode redirecionar para a página principal do sistema
    } else {
        alert("Usuário ou senha incorretos. Tente novamente.");
    }
}