$("#submit_form").on("submit",async function(e){
    e.preventDefault()
    const $in_val = $("#guess").val()
    const response = axios.get("/check_word",{params:{word:$in_val}})
    alert(response) 
})