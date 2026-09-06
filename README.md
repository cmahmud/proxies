# SyndProxy validated proxy pool

## Current pool

- Alive now: 422
- Gold now: 324
- HTTP: 82 alive / 56 gold
- HTTPS: 37 alive / 13 gold
- SOCKS4: 153 alive / 133 gold
- SOCKS5: 150 alive / 122 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48347
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
