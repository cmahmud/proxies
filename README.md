# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 404
- HTTP: 103 alive / 58 gold
- HTTPS: 75 alive / 17 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39128
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
