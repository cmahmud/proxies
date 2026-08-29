# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 387
- HTTP: 87 alive / 67 gold
- HTTPS: 69 alive / 13 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 166 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43368
- Ever gold: 1370

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
