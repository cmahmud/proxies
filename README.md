# SyndProxy validated proxy pool

## Current pool

- Alive now: 413
- Gold now: 329
- HTTP: 79 alive / 54 gold
- HTTPS: 41 alive / 17 gold
- SOCKS4: 145 alive / 134 gold
- SOCKS5: 148 alive / 124 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48344
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
