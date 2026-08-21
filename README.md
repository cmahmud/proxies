# SyndProxy private pool

## Current pool

- Alive now: 1369
- Gold now: 461
- HTTP: 512 alive / 112 gold
- HTTPS: 361 alive / 29 gold
- SOCKS4: 238 alive / 160 gold
- SOCKS5: 258 alive / 160 gold

## Historical pool

- Discovered: 160011
- Ever alive: 30510
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
