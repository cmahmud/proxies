# SyndProxy private pool

## Current pool

- Alive now: 944
- Gold now: 345
- HTTP: 294 alive / 50 gold
- HTTPS: 184 alive / 15 gold
- SOCKS4: 230 alive / 141 gold
- SOCKS5: 236 alive / 139 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14686
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
