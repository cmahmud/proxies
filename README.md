# SyndProxy validated proxy pool

## Current pool

- Alive now: 436
- Gold now: 335
- HTTP: 89 alive / 57 gold
- HTTPS: 51 alive / 18 gold
- SOCKS4: 150 alive / 134 gold
- SOCKS5: 146 alive / 126 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48345
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
