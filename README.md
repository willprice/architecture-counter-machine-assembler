# Assembler

## Functionality
* Ignore stuff after and including `;`
* Ignore whitespace
* We need to translate INC, DEC, JNZ, JNEG, STR, and LDR to their corresponding
opcods and operands.
* Resolve labels
* Labels start with `:`
* Output should be to a hex file with the format `<instruction><newline>`
* For debugging purposes output line numbers 

## Tests
To run the tests you must have nose installed, once installed run `nosetests` in
the top directory.
