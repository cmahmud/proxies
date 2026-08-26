# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 379
- HTTP: 107 alive / 62 gold
- HTTPS: 62 alive / 18 gold
- SOCKS4: 154 alive / 145 gold
- SOCKS5: 174 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38896
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
