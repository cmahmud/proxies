# SyndProxy private pool

## Current pool

- Alive now: 920
- Gold now: 278
- HTTP: 342 alive / 37 gold
- HTTPS: 198 alive / 10 gold
- SOCKS4: 216 alive / 139 gold
- SOCKS5: 164 alive / 92 gold

## Historical pool

- Discovered: 102917
- Ever alive: 13932
- Ever gold: 432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
