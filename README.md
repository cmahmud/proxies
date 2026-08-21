# SyndProxy private pool

## Current pool

- Alive now: 919
- Gold now: 377
- HTTP: 277 alive / 85 gold
- HTTPS: 236 alive / 29 gold
- SOCKS4: 181 alive / 124 gold
- SOCKS5: 225 alive / 139 gold

## Historical pool

- Discovered: 153751
- Ever alive: 28855
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
