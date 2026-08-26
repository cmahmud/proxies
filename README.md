# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 377
- HTTP: 106 alive / 62 gold
- HTTPS: 66 alive / 18 gold
- SOCKS4: 156 alive / 145 gold
- SOCKS5: 178 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38898
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
