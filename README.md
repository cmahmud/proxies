# SyndProxy private pool

## Current pool

- Alive now: 650
- Gold now: 368
- HTTP: 167 alive / 68 gold
- HTTPS: 112 alive / 17 gold
- SOCKS4: 180 alive / 142 gold
- SOCKS5: 191 alive / 141 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25650
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
