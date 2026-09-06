# SyndProxy validated proxy pool

## Current pool

- Alive now: 413
- Gold now: 308
- HTTP: 80 alive / 61 gold
- HTTPS: 30 alive / 14 gold
- SOCKS4: 148 alive / 121 gold
- SOCKS5: 155 alive / 112 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48382
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
