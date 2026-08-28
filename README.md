# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 395
- HTTP: 100 alive / 69 gold
- HTTPS: 85 alive / 14 gold
- SOCKS4: 161 alive / 152 gold
- SOCKS5: 176 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43186
- Ever gold: 1366

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
