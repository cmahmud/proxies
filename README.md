# SyndProxy private pool

## Current pool

- Alive now: 1113
- Gold now: 542
- HTTP: 410 alive / 159 gold
- HTTPS: 277 alive / 107 gold
- SOCKS4: 218 alive / 132 gold
- SOCKS5: 208 alive / 144 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19836
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
