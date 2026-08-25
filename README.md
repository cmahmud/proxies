# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 394
- HTTP: 103 alive / 62 gold
- HTTPS: 72 alive / 19 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 159 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37523
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
