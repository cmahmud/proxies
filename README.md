# SyndProxy private pool

## Current pool

- Alive now: 785
- Gold now: 382
- HTTP: 238 alive / 86 gold
- HTTPS: 131 alive / 21 gold
- SOCKS4: 191 alive / 126 gold
- SOCKS5: 225 alive / 149 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31389
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
