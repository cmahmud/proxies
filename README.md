# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 403
- HTTP: 256 alive / 86 gold
- HTTPS: 175 alive / 24 gold
- SOCKS4: 215 alive / 139 gold
- SOCKS5: 246 alive / 154 gold

## Historical pool

- Discovered: 151689
- Ever alive: 27793
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
