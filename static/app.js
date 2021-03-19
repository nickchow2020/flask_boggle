let score = 0
let timeOut = 60
let plays = 0

$("#submit_form").on("submit",async function(e){
    e.preventDefault()
    const $in_val = $("#guess").val()
    const response = await axios.get("/check_word",{params:{word:$in_val}})
    if(response.data.result === "not-word"){
        $("#show_msg").text("Letters guess are not a valid words")
    }else if(response.data.result === "not-not-on-board"){
        $("#show_msg").text("Letters guess are not game board,please try again")
    }else{
        $("#show_msg").text("Letters guess are founds,Congratulations!")
        score += $in_val.length
    }

    $("#guess").val("")
    $("#score").text(score)
    plays += 1
})

const timer = setInterval(async function(){
    timeOut -= 1
    $("#timeOut").text(timeOut)
    if(timeOut === 0){
        clearInterval(timer)
        $("#guess").prop("disabled",true)
        const response = await axios.post("/post_score",{score,plays})
        if (response.data){
            $("#show_msg").text("Your Break the Record,Great Job!")
        }else{
            $("#show_msg").text("You done a Great Job")
        }
    } 
},1000)