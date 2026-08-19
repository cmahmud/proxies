# SyndProxy private pool

## Current pool

- Alive now: 1303
- Gold now: 415
- HTTP: 452 alive / 94 gold
- HTTPS: 287 alive / 19 gold
- SOCKS4: 255 alive / 142 gold
- SOCKS5: 309 alive / 160 gold

## Historical pool

- Discovered: 131823
- Ever alive: 20962
- Ever gold: 877

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
