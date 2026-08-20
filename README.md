# SyndProxy private pool

## Current pool

- Alive now: 1892
- Gold now: 704
- HTTP: 704 alive / 235 gold
- HTTPS: 609 alive / 147 gold
- SOCKS4: 241 alive / 157 gold
- SOCKS5: 338 alive / 165 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24422
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
