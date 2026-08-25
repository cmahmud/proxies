# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 421
- HTTP: 87 alive / 70 gold
- HTTPS: 48 alive / 22 gold
- SOCKS4: 213 alive / 162 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37125
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
