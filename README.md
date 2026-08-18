# SyndProxy private pool

## Current pool

- Alive now: 651
- Gold now: 260
- HTTP: 146 alive / 29 gold
- HTTPS: 89 alive / 6 gold
- SOCKS4: 216 alive / 132 gold
- SOCKS5: 200 alive / 93 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9108
- Ever gold: 363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
