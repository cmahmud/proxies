# SyndProxy private pool

## Current pool

- Alive now: 788
- Gold now: 381
- HTTP: 232 alive / 85 gold
- HTTPS: 139 alive / 21 gold
- SOCKS4: 193 alive / 126 gold
- SOCKS5: 224 alive / 149 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31391
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
