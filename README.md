# SyndProxy private pool

## Current pool

- Alive now: 1381
- Gold now: 457
- HTTP: 524 alive / 107 gold
- HTTPS: 361 alive / 29 gold
- SOCKS4: 241 alive / 160 gold
- SOCKS5: 255 alive / 161 gold

## Historical pool

- Discovered: 160011
- Ever alive: 30512
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
