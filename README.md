# SyndProxy private pool

## Current pool

- Alive now: 636
- Gold now: 256
- HTTP: 167 alive / 31 gold
- HTTPS: 88 alive / 8 gold
- SOCKS4: 200 alive / 133 gold
- SOCKS5: 181 alive / 84 gold

## Historical pool

- Discovered: 94348
- Ever alive: 9687
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
