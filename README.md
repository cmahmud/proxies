# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 405
- HTTP: 102 alive / 64 gold
- HTTPS: 95 alive / 14 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 191 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38079
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
