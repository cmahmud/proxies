# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 409
- HTTP: 114 alive / 70 gold
- HTTPS: 80 alive / 21 gold
- SOCKS4: 162 alive / 158 gold
- SOCKS5: 170 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37177
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
