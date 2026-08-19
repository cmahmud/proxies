# SyndProxy private pool

## Current pool

- Alive now: 1463
- Gold now: 421
- HTTP: 542 alive / 88 gold
- HTTPS: 373 alive / 18 gold
- SOCKS4: 260 alive / 156 gold
- SOCKS5: 288 alive / 159 gold

## Historical pool

- Discovered: 131815
- Ever alive: 20859
- Ever gold: 876

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
