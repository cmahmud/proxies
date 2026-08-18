# SyndProxy private pool

## Current pool

- Alive now: 641
- Gold now: 263
- HTTP: 165 alive / 34 gold
- HTTPS: 96 alive / 10 gold
- SOCKS4: 198 alive / 134 gold
- SOCKS5: 182 alive / 85 gold

## Historical pool

- Discovered: 94348
- Ever alive: 9687
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
