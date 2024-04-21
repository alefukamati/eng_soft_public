let resultados = false;

//exibir resultado

if (resultados) {
  const prediposicao = document.getElementById("predisposicao");
  prediposicao.textContent = "POSSUI PREDISPOSIÇÃO";
} else if (resultados == false) {
  const prediposicao = document.getElementById("predisposicao");
  prediposicao.textContent = "NÃO POSSUI PREDISPOSIÇÃO";
}

//scroll entenda resultado
if (resultados) {
}
document
  .getElementById("entenderResultado")
  .addEventListener("click", function () {
    const targetElement = document.getElementById("explicacao");
    const targetPosition = targetElement.offsetTop;
    window.scrollTo({
      top: targetPosition,
      behavior: "smooth",
    });
  });

document.getElementById("enviarEmail").addEventListener("click", function () {
  alert("EMAIL ENVIADO"); //PRECISA FAZER SISTEMA QUE ENVIA EMAIL
});

//ocultar explicacao
if (resultados) {
  const explicacaoPositivo = document.getElementById("explicacaoPositivo");
  explicacaoPositivo.style.display = "flex";
} else if (resultados == false) {
  const explicacaoNegativo = document.getElementById("explicacaoNegativo");
  explicacaoNegativo.style.display = "flex";
}
