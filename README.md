# SyndProxy private pool

## Current pool

- Alive now: 645
- Gold now: 347
- HTTP: 168 alive / 69 gold
- HTTPS: 106 alive / 18 gold
- SOCKS4: 176 alive / 124 gold
- SOCKS5: 195 alive / 136 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25576
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
