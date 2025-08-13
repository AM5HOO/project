//first game ever
let playGame = confirm("Shall we play rock, paper or scissors?");
if (playGame) {
    //play 
    let playerChoice = prompt("Please enter rock, paper or scissors.");
    if (playerChoice) {
        let playerOne = playerChoice.trim().toLowerCase();
        if (playerOne === "rock" || playerOne === "paper" || playerOne === "scissors") {
            
            let computerChoice = Math.floor(Math.random() * 3 + 1);
            let computer = computerChoice === 1 ? "rock"
            : computerChoice === 2 ? "paper"
            : "scissors";

            let result =
            playerOne === computer
            ? "Tie game!"
            : playerOne === "rock" && computer === "paper"
            ? `You: ${playerOne}\nComputer: ${computer}\nComputer wins!`
            : playerOne === "paper" && computer === "scissors"
            ? `You: ${playerOne}\nComputer: ${computer}\nComputer wins!`
            : playerOne === "scissors" && computer === "rock"
            ? `You: ${playerOne}\nComputer: ${computer}\nComputer wins!`
            : `You: ${playerOne}\nComputer: ${computer}\n You won!`;
            alert(result);
            let playAgain = confirm("play again?")
            playAgain
            ? location.reload() 
            : alert("Thanks for playing!");
                
        }

            } else {
        alert("I guess you changed your mind. Maybe next time.");
    }
} else {
    alert("Okay, maybe next time, yeah?");

}