# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 429
- HTTP: 317 alive / 94 gold
- HTTPS: 208 alive / 23 gold
- SOCKS4: 219 alive / 160 gold
- SOCKS5: 235 alive / 152 gold

## Historical pool

- Discovered: 158253
- Ever alive: 30062
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
