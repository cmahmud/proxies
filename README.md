# SyndProxy private pool

## Current pool

- Alive now: 1385
- Gold now: 402
- HTTP: 476 alive / 88 gold
- HTTPS: 373 alive / 17 gold
- SOCKS4: 230 alive / 150 gold
- SOCKS5: 306 alive / 147 gold

## Historical pool

- Discovered: 134448
- Ever alive: 21809
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
