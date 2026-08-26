# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 395
- HTTP: 103 alive / 63 gold
- HTTPS: 46 alive / 16 gold
- SOCKS4: 162 alive / 156 gold
- SOCKS5: 180 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38934
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
