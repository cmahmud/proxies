# SyndProxy private pool

## Current pool

- Alive now: 765
- Gold now: 408
- HTTP: 204 alive / 83 gold
- HTTPS: 142 alive / 27 gold
- SOCKS4: 205 alive / 139 gold
- SOCKS5: 214 alive / 159 gold

## Historical pool

- Discovered: 162441
- Ever alive: 31429
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
