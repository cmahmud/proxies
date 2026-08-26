# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 405
- HTTP: 108 alive / 63 gold
- HTTPS: 55 alive / 19 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38956
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
