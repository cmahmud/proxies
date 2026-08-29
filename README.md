# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 419
- HTTP: 108 alive / 78 gold
- HTTPS: 66 alive / 29 gold
- SOCKS4: 156 alive / 153 gold
- SOCKS5: 167 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43655
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
