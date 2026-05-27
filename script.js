const fileInput = document.getElementById('file-upload');
const analyzeBtn = document.getElementById('analyze-btn');
const resultText = document.getElementById('result-text');

analyzeBtn.addEventListener('click', function(){
    const file = fileInput.files[0];
    if (!file) {
        resultText.textContent = 'Por favor, escolha uma imagem primeiro.';
        return;
    }
    const formData = new FormData();
    formData.append('file', file);

    resultText.textContent = 'Analisando...';

    fetch('https://ai-detector-api-mk6b.onrender.com/analyze', {
        method: 'POST',
        body: formData
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        const emoji = data.is_ai_generated ? '🤖' : '✅';
        const status = data.is_ai_generated ? 'Imagem gerada por IA': 'Imagem real';
        const confidence = Math.round(data.confidence * 100);

        resultText.textContent = emoji + ' ' + status + ' - ' + confidence + '% de confiança';
    })
    .catch(function(error) {
        resultText.textContent = 'Erro ao conectar com API. Verifique se o servidor está rodando.';
        console.error('Erro:', error);
    });

})