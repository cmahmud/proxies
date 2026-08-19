# SyndProxy private pool

## Current pool

- Alive now: 1371
- Gold now: 415
- HTTP: 510 alive / 86 gold
- HTTPS: 329 alive / 16 gold
- SOCKS4: 263 alive / 157 gold
- SOCKS5: 269 alive / 156 gold

## Historical pool

- Discovered: 131814
- Ever alive: 20809
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
