# SyndProxy validated proxy pool

## Current pool

- Alive now: 388
- Gold now: 322
- HTTP: 69 alive / 51 gold
- HTTPS: 27 alive / 10 gold
- SOCKS4: 146 alive / 137 gold
- SOCKS5: 146 alive / 124 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48321
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
