# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 404
- HTTP: 312 alive / 87 gold
- HTTPS: 235 alive / 19 gold
- SOCKS4: 228 alive / 148 gold
- SOCKS5: 261 alive / 150 gold

## Historical pool

- Discovered: 158238
- Ever alive: 30007
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
