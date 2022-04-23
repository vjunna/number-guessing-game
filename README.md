# random-guess-game
A simple random number guessing game

User gets 7 chances to correctly guess a number between '0' and '9'

```mermaid
graph TD;

    Start -->Yes;
    Start -->No;

    Yes -->7_Tries;
    No -->Exit;

    7_Tries -->Win;
    7_Tries -->Retry;

    Win -->Start;
    Retry -->7_Tries;
    Retry -->Lost;
    Lost -->Start;
```
