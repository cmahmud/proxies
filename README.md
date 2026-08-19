# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 396
- HTTP: 328 alive / 100 gold
- HTTPS: 246 alive / 20 gold
- SOCKS4: 195 alive / 127 gold
- SOCKS5: 290 alive / 149 gold

## Historical pool

- Discovered: 136224
- Ever alive: 22522
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
