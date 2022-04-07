# random-guess-game
A simple random number guessing game

User gets 7 chances to correctly guess a number between '0' and '9'

```mermaid
graph TD;

    Start -->Yes;
    Start -->No;

    Yes -->Guess_Num_7_Times;
    No -->Exit;

    Guess_Num_7_Times -->Win;
    Guess_Num_7_Times -->Retry;

    Win -->Start;
    Retry -->Guess_Num_7_Times
    Retry -->Lost
    Lost -->Start
```
