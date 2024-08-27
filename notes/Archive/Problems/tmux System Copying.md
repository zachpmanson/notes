[[tmux System Copying]] is dogshit at copying by default.

To allow it to pipe to the normal system clipboard:

```
bind -T copy-mode-vi y send-keys -X copy-pipe-and-cancel 'pbcopy'
```

