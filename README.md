# SyndProxy private pool

## Current pool

- Alive now: 694
- Gold now: 379
- HTTP: 181 alive / 71 gold
- HTTPS: 89 alive / 15 gold
- SOCKS4: 208 alive / 138 gold
- SOCKS5: 216 alive / 155 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25802
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
