# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 408
- HTTP: 95 alive / 61 gold
- HTTPS: 79 alive / 21 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37037
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
