# SyndProxy validated proxy pool

## Current pool

- Alive now: 393
- Gold now: 314
- HTTP: 74 alive / 52 gold
- HTTPS: 31 alive / 9 gold
- SOCKS4: 146 alive / 132 gold
- SOCKS5: 142 alive / 121 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48330
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
