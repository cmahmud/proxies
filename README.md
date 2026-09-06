# SyndProxy validated proxy pool

## Current pool

- Alive now: 413
- Gold now: 341
- HTTP: 80 alive / 59 gold
- HTTPS: 29 alive / 12 gold
- SOCKS4: 144 alive / 137 gold
- SOCKS5: 160 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48385
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
