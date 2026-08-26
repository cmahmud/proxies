# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 408
- HTTP: 116 alive / 66 gold
- HTTPS: 74 alive / 18 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 200 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38691
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
