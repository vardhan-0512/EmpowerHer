/*async function submitMood() {
    const input_mood = document.getElementById('input_mood').value;

    const response = await fetch('http://127.0.0.1:8000/mood', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input_mood })
    });

    const data = await response.json();
    document.getElementById('result').innerText = `Predicted mood: ${JSON.stringify(data)}`;
}*/
const form = document.querySelector("form"),
        nextBtn = form.querySelector(".nextBtn"),
        backBtn = form.querySelector(".backBtn"),
        allInput = form.querySelectorAll(".first input");
nextBtn.addEventListener("click", ()=> {
    allInput.forEach(input => {
        if(input.value != ""){
            form.classList.add('secActive');
        }else{
            form.classList.remove('secActive');
        }
    })
})
