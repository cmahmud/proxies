# SyndProxy private pool

## Current pool

- Alive now: 966
- Gold now: 345
- HTTP: 318 alive / 50 gold
- HTTPS: 193 alive / 11 gold
- SOCKS4: 231 alive / 145 gold
- SOCKS5: 224 alive / 139 gold

## Historical pool

- Discovered: 107065
- Ever alive: 14650
- Ever gold: 468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
