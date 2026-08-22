# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 364
- HTTP: 341 alive / 79 gold
- HTTPS: 227 alive / 24 gold
- SOCKS4: 217 alive / 124 gold
- SOCKS5: 256 alive / 137 gold

## Historical pool

- Discovered: 165819
- Ever alive: 32331
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
