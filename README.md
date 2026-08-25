# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 405
- HTTP: 90 alive / 64 gold
- HTTPS: 73 alive / 19 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37674
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
