# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 407
- HTTP: 100 alive / 62 gold
- HTTPS: 74 alive / 16 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39115
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
