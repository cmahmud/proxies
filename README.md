# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 346
- HTTP: 341 alive / 53 gold
- HTTPS: 185 alive / 14 gold
- SOCKS4: 230 alive / 139 gold
- SOCKS5: 236 alive / 140 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14690
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
