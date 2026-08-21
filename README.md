# SyndProxy private pool

## Current pool

- Alive now: 1360
- Gold now: 444
- HTTP: 521 alive / 109 gold
- HTTPS: 338 alive / 33 gold
- SOCKS4: 233 alive / 137 gold
- SOCKS5: 268 alive / 165 gold

## Historical pool

- Discovered: 159270
- Ever alive: 30375
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
