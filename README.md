# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 399
- HTTP: 94 alive / 54 gold
- HTTPS: 78 alive / 16 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39141
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
