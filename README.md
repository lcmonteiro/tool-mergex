# tool-mergex

## install

### git config

First up is defining the merge driver.
This is done in the `.gitconfig` or `.git/config` file:

```
[merge "mergex-arxml"]
	name = A custom merge driver used to resolve conflicts in XML files
	driver = mergex %A %O %B --type arxml 
[merge "mergex-xdm"]
	name = A custom merge driver used to resolve conflicts in XML files
	driver = mergex %A %O %B --type xdm
```

### git attributes

Configure the file patterns that you want to use mergex as a merger tool in the `.gitattributes` or `.git/info/attributes` file:

```
*.arxml merge=mergex-arxml
*.xdm   merge=mergex-xdm
```
