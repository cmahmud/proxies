# SyndProxy private pool

## Current pool

- Alive now: 953
- Gold now: 403
- HTTP: 289 alive / 95 gold
- HTTPS: 216 alive / 24 gold
- SOCKS4: 240 alive / 156 gold
- SOCKS5: 208 alive / 128 gold

## Historical pool

- Discovered: 160980
- Ever alive: 30839
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
