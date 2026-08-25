# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 410
- HTTP: 92 alive / 62 gold
- HTTPS: 71 alive / 21 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37039
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
