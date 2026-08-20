# SyndProxy private pool

## Current pool

- Alive now: 1160
- Gold now: 393
- HTTP: 389 alive / 97 gold
- HTTPS: 287 alive / 27 gold
- SOCKS4: 236 alive / 133 gold
- SOCKS5: 248 alive / 136 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25120
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
