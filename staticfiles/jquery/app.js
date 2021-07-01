$(function () {
    let saldo = $("#saldo").text();
    saldo_convertido = saldo.replace(",", ".");
    trocaCorSaldo(parseFloat(saldo_convertido));
    console.log("Estamos rodando!");
    console.log(saldo_convertido);
});


function trocaCorSaldo(saldo) {
    let texto_saldo = $("#texto_saldo");
    let borda_saldo = $("#borda_saldo");

    if (saldo <= 0) {
        texto_saldo.removeClass("text-primary");
        borda_saldo.removeClass("border-bottom-primary");
        texto_saldo.addClass("text-danger");
        borda_saldo.addClass("border-bottom-danger");
    } else {
        texto_saldo.removeClass("text-danger");
        borda_saldo.removeClass("border-bottom-danger");
        texto_saldo.addClass("text-primary");
        borda_saldo.addClass("border-bottom-primary");
    }
}
