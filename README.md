# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 420
- HTTP: 111 alive / 71 gold
- HTTPS: 69 alive / 21 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37116
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
