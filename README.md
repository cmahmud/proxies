# SyndProxy private pool

## Current pool

- Alive now: 1154
- Gold now: 396
- HTTP: 379 alive / 98 gold
- HTTPS: 289 alive / 27 gold
- SOCKS4: 235 alive / 134 gold
- SOCKS5: 251 alive / 137 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25123
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
