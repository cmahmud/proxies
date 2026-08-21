# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 429
- HTTP: 338 alive / 91 gold
- HTTPS: 218 alive / 26 gold
- SOCKS4: 217 alive / 151 gold
- SOCKS5: 236 alive / 161 gold

## Historical pool

- Discovered: 156425
- Ever alive: 29500
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
