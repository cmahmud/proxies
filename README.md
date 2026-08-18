# SyndProxy private pool

## Current pool

- Alive now: 645
- Gold now: 257
- HTTP: 147 alive / 30 gold
- HTTPS: 87 alive / 6 gold
- SOCKS4: 216 alive / 133 gold
- SOCKS5: 195 alive / 88 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9108
- Ever gold: 363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
