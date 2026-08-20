# SyndProxy private pool

## Current pool

- Alive now: 1878
- Gold now: 704
- HTTP: 690 alive / 240 gold
- HTTPS: 603 alive / 145 gold
- SOCKS4: 248 alive / 157 gold
- SOCKS5: 337 alive / 162 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24418
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
