# SyndProxy private pool

## Current pool

- Alive now: 995
- Gold now: 423
- HTTP: 332 alive / 90 gold
- HTTPS: 219 alive / 23 gold
- SOCKS4: 203 alive / 148 gold
- SOCKS5: 241 alive / 162 gold

## Historical pool

- Discovered: 156425
- Ever alive: 29500
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
