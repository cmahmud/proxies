# SyndProxy private pool

## Current pool

- Alive now: 1069
- Gold now: 390
- HTTP: 326 alive / 98 gold
- HTTPS: 218 alive / 25 gold
- SOCKS4: 259 alive / 131 gold
- SOCKS5: 266 alive / 136 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25090
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
