# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 347
- HTTP: 98 alive / 38 gold
- HTTPS: 49 alive / 10 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 166 alive / 148 gold

## Historical pool

- Discovered: 171059
- Ever alive: 32858
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
