# SyndProxy validated proxy pool

## Current pool

- Alive now: 414
- Gold now: 312
- HTTP: 82 alive / 50 gold
- HTTPS: 42 alive / 10 gold
- SOCKS4: 145 alive / 134 gold
- SOCKS5: 145 alive / 118 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48367
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
