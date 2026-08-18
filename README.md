# SyndProxy private pool

## Current pool

- Alive now: 641
- Gold now: 255
- HTTP: 168 alive / 30 gold
- HTTPS: 94 alive / 8 gold
- SOCKS4: 202 alive / 133 gold
- SOCKS5: 177 alive / 84 gold

## Historical pool

- Discovered: 94348
- Ever alive: 9683
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
