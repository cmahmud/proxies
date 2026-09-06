# SyndProxy validated proxy pool

## Current pool

- Alive now: 413
- Gold now: 330
- HTTP: 81 alive / 58 gold
- HTTPS: 28 alive / 11 gold
- SOCKS4: 147 alive / 134 gold
- SOCKS5: 157 alive / 127 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48383
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
