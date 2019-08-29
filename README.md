# tool-mergex

## install

### git config

First up is defining the merge driver.
This is done in the `.gitconfig` file:

```
[merge "mergex"]
	name = A custom merge driver used to resolve conflicts in XML files
	driver = mergex %A %O %B
```

### git attributes

Configure the file patterns that you want to use mergex as a merger tool in the `.gitattributes` file:

```
*.axml merge=mergex
*.xdm  merge=mergex
```
