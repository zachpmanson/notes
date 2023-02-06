Vi is a text editor created for Unix by Bill Joy in 1976. Its name is short for for visual mode, as it was a originally only a visual interface for ex, a line editor created by Joy and Chuck Haley. Its name has spawned the backronym visual interface.

Vim (Vi IMproved) is an expanded clone of Vim created by Bram Moolenaar in 1991. 

## Movement Origins

Vi uses hjkl for navigation as it was developed on an ADM-3A terminal which didn't have dedicated arrow keys, using hjkl for navigation.

![[ADM3A.png]]
The placement of control and escape are also different to modern QWERTY keyboards, and is the reason that the Escape key is so heavily used in Vi.

The reason that the ADM-3A used hjkl for navigation is due to the ASCII standard.  The first 32 characters are control characters, used for in-band signaling to cause effects other than representable written symbols. Control characters can be invoked by holding the Control key in conjuction with other keys. The keys used are determined by running XOR on the first bit of the ASCII character.  For example, D is 1000100.  XOR on the first digit results in 0000100 which is the ASCII control character EOT (end of transmission).  This is why pressing Ctrl-D on modern terminals exits the terminal. Ctrl-I follows a similar pattern, aligning with TAB, which  works in modern terminals as well.

Applying this to Ctrl-H results in BS (backspace), which is why H was chosen to move the the cursor back one space on the ADM-3A. Applying this to Ctrl-J results in LF (line feed, a new line), which is why J was chosen to move the cursor down one line on the ADM-3A. For conceptual symmetry K and L became the inverses of these, though Ctrl-K corresponds to VT (vertical tab), and Ctrl-L corresponds to FF (form feed, similar to a pagebreak).  These were both useful control characters in the contexts of printing terminals but less  broadly applicable for screen based terminals like the ADM-3A.

I first learnt of this was [here](https://twitter.com/hillelogram/status/1326600125569961991), which links to [this table](https://sltls.org/ASCII) which greatly helps in visualising this property.