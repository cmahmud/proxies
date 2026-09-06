# SyndProxy validated proxy pool

## Current pool

- Alive now: 403
- Gold now: 331
- HTTP: 73 alive / 54 gold
- HTTPS: 40 alive / 18 gold
- SOCKS4: 142 alive / 133 gold
- SOCKS5: 148 alive / 126 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48339
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
