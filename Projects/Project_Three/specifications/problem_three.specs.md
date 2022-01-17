# Problem Three Specifications

In a Canadian postal code (zip code), the first, third and fifth characters are letters, while the second, fourth and sixth characters are digits. There is a space between the third and fourth characters for a total length of 7. A Canadian province can be determined from the first character of a postal code, as shown in the table below. No valid postal codes currently begin with D, F, I, O, Q, U, W, or Z. 

## Create a dictionary from this table:

| Province | First Character(s) |
| -------- | -----------------: |
| Newfoundland | A |
| Nova Scotia | B |
| Prince Edward Island | C |
| New Brunswick | E |
| Quebec | G H J |
| Ontario | K L M N P |
| Manitoba | R |
| Saskatchewan | S |
| Alberta | T |
| British Columbia | V |
| Nunavut | X |
| Northwest Territories | X |
| Yukon | Y |

*Note that the letter X can mean Nunavut or Northwest Territories. The second character indicates rural or urban addresses: 0 means a rural address, anything else an urban address.*

- Write a program that loops to read a postal code from a user. 
- The program ends when the user presses just the `<Enter>` key in response to your prompt. 
- If the user entered a postal code, validate it first. 
- The string must be seven characters long (otherwise it is invalid) and cannot begin with the letters D, F, I, O, Q, U, W, or Z (which would make the entry invalid).
- If the first letter is valid, display the province associated with the letter and whether the address is urban or rural.
- For example, for T2N 1N4, your program should display that the address is an urban one in Alberta. For X0A 1B2, your program should display that the address is a rural one in Nunavut or Northwest Territories.
- Display a meaningful message if the postal code is invalid. 