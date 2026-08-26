# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 408
- HTTP: 96 alive / 64 gold
- HTTPS: 71 alive / 15 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39235
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
