# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 416
- HTTP: 92 alive / 66 gold
- HTTPS: 72 alive / 22 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37046
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
