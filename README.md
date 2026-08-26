# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 387
- HTTP: 102 alive / 63 gold
- HTTPS: 69 alive / 22 gold
- SOCKS4: 153 alive / 145 gold
- SOCKS5: 175 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38763
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
