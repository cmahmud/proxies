# SyndProxy private pool

## Current pool

- Alive now: 1492
- Gold now: 611
- HTTP: 571 alive / 221 gold
- HTTPS: 469 alive / 117 gold
- SOCKS4: 215 alive / 133 gold
- SOCKS5: 237 alive / 140 gold

## Historical pool

- Discovered: 140789
- Ever alive: 23781
- Ever gold: 961

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
