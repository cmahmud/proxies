# SyndProxy private pool

## Current pool

- Alive now: 957
- Gold now: 403
- HTTP: 276 alive / 95 gold
- HTTPS: 217 alive / 34 gold
- SOCKS4: 218 alive / 143 gold
- SOCKS5: 246 alive / 131 gold

## Historical pool

- Discovered: 160995
- Ever alive: 30942
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
