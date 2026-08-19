# SyndProxy private pool

## Current pool

- Alive now: 1069
- Gold now: 520
- HTTP: 369 alive / 160 gold
- HTTPS: 265 alive / 89 gold
- SOCKS4: 214 alive / 139 gold
- SOCKS5: 221 alive / 132 gold

## Historical pool

- Discovered: 119875
- Ever alive: 18514
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
