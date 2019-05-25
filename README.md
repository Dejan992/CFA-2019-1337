# CFA-2019-1337
Bruteforcing our way towards ultimate customer satisfaction- free food! **(For Educational Purposes Only, Use at Your Own Discretion)**

Analyzing multiple receipts from Chick-fil-As across the country (via Google Images) allowed us to determine (roughly) the pattern used for generating the "Serial Num" occasionally found near the bottom of the customer copy receipt (see example below).

Insecurities in their [customer experience portal](https://www.mycfavisit.com) allow for these serial numbers to be verified as working in rapid succession. Once a given serial number as been verified as working, using a web browser automation library like Selenium, the customer experience survey can be completed automatically (and auto-filled with the email you'd like to have your free sandwich voucher(s) sent to).

### Example Serial Num: 6320106-01336-1109-0523-95

**Sequence 1 (7-Digits)**
- Out of the first sequence of seven digits, the first three represent the last three digits of the **Order Number**, printed near the top of the customer copy receipt (in this case, the order number was 5222**632**).
- The 4th and 6th digits of this first sequence will always be zero (632**0**1**0**6).
- The 5th digit is assumed to be the revenue center (dine-in, carry-out, drive-thru), in this case dine-in was represented by a 1 (printed below the date/time on the customer copy).
- The 7th digit of this first sequence represents the register that the transaction was carried out on (printed above the cashier name on the customer copy), in this case, register 6.

**Sequence 2 (5-Digits)**
- The five-digit number that makes up sequence two is simply the store number printed near the top of the receipt (in this case, #01336).

**Sequence 3 & 4 (4-Digits Each)**
- Sequence 3 represents the time of the transaction (HH:MM), followed by the date that the transaction was made on (MM:DD).

**Sequence 5 (2-Digits)**
- The first of the two digits in the last sequence is the last number of the year that the transation was made in (9, as of 2019).
- What the second of the last two digits in this sequence represents has not **yet** been determined.
