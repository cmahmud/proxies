# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 396
- HTTP: 89 alive / 66 gold
- HTTPS: 90 alive / 14 gold
- SOCKS4: 159 alive / 154 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43229
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
