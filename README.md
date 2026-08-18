# SyndProxy private pool

## Current pool

- Alive now: 1341
- Gold now: 230
- HTTP: 614 alive / 29 gold
- HTTPS: 255 alive / 8 gold
- SOCKS4: 237 alive / 109 gold
- SOCKS5: 235 alive / 84 gold

## Historical pool

- Discovered: 86746
- Ever alive: 7588
- Ever gold: 335

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
