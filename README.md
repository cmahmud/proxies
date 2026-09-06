# SyndProxy validated proxy pool

## Current pool

- Alive now: 413
- Gold now: 334
- HTTP: 81 alive / 59 gold
- HTTPS: 29 alive / 9 gold
- SOCKS4: 142 alive / 134 gold
- SOCKS5: 161 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48385
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
