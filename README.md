# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 401
- HTTP: 99 alive / 69 gold
- HTTPS: 76 alive / 20 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 168 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37452
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
