# SyndProxy validated proxy pool

## Current pool

- Alive now: 416
- Gold now: 324
- HTTP: 82 alive / 54 gold
- HTTPS: 36 alive / 15 gold
- SOCKS4: 150 alive / 134 gold
- SOCKS5: 148 alive / 121 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48347
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
