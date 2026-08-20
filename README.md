# SyndProxy private pool

## Current pool

- Alive now: 1181
- Gold now: 569
- HTTP: 437 alive / 191 gold
- HTTPS: 290 alive / 95 gold
- SOCKS4: 229 alive / 148 gold
- SOCKS5: 225 alive / 135 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22852
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
