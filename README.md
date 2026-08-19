# SyndProxy private pool

## Current pool

- Alive now: 1073
- Gold now: 419
- HTTP: 328 alive / 86 gold
- HTTPS: 234 alive / 16 gold
- SOCKS4: 225 alive / 159 gold
- SOCKS5: 286 alive / 158 gold

## Historical pool

- Discovered: 134522
- Ever alive: 21839
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
