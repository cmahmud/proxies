# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 413
- HTTP: 97 alive / 67 gold
- HTTPS: 70 alive / 18 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 172 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37089
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
