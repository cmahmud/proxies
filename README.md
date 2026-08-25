# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 395
- HTTP: 95 alive / 63 gold
- HTTPS: 73 alive / 19 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 162 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37526
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
