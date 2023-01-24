



var responseLength = 140
var inputText = ''
var outputText = ''
var sliderEl = document.getElementById("myRange");
var textInputEl = document.getElementById("input-text");
var textOutputEl = document.getElementById("output");
var loadingIconEL = document.getElementById("loadingIcon")
// Update the current slider value (each time you drag the slider handle)
sliderEl.oninput = function() {
  document.getElementById("length-slide").innerText=this.value;
  responseLength = this.value
}

function getResponse(){
    inputText = textInputEl.value
    console.log(responseLength,inputText)
    loadingIconEL.style.opacity = 1;
    $.ajax(
        {
            type:"GET",
            url: "/request/",
            
            dataType: 'json',
            data:{
            length: responseLength,

            text: inputText,
            },
            success: function(asdf) {
            //document.getElementById("loadingIcon").style.opacity = 0;
            loadingIconEL.style.opacity = 0;
            outputText = asdf.r
            textOutputEl.innerText=outputText
            //document.getElementById("num").innerText = 'Number is: '+number
           

        }
        })

        return outputText

}

