# SyndProxy private pool

## Current pool

- Alive now: 1232
- Gold now: 417
- HTTP: 432 alive / 84 gold
- HTTPS: 268 alive / 17 gold
- SOCKS4: 236 alive / 159 gold
- SOCKS5: 296 alive / 157 gold

## Historical pool

- Discovered: 134522
- Ever alive: 21878
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
