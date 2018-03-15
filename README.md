# Fishes and crayfishes.
Rulesets have the following format:

```<replace this symbol><with this one><if this regex matches>```

The regex will be matched with the neighboring tiles represented as a string starting from the top left one and going clocwise. Example:

```_#[^0]*```

This will replace all _s that have no neighboring 0s with a #.

States are saved exactly like one would expect.

Standard ruleset uses ~ for fishes, ; for crayfishes, . for blanks and # for rocks.
