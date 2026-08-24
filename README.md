# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 430
- HTTP: 134 alive / 74 gold
- HTTPS: 79 alive / 25 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34605
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
