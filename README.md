# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 413
- HTTP: 92 alive / 66 gold
- HTTPS: 76 alive / 22 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 177 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37782
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
