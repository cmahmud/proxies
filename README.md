# SyndProxy private pool

## Current pool

- Alive now: 1317
- Gold now: 434
- HTTP: 438 alive / 95 gold
- HTTPS: 309 alive / 25 gold
- SOCKS4: 254 alive / 147 gold
- SOCKS5: 316 alive / 167 gold

## Historical pool

- Discovered: 136220
- Ever alive: 22462
- Ever gold: 901

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
