# SyndProxy validated proxy pool

## Current pool

- Alive now: 413
- Gold now: 318
- HTTP: 79 alive / 54 gold
- HTTPS: 39 alive / 10 gold
- SOCKS4: 148 alive / 134 gold
- SOCKS5: 147 alive / 120 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48348
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
