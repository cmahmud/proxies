# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 396
- HTTP: 93 alive / 69 gold
- HTTPS: 93 alive / 16 gold
- SOCKS4: 161 alive / 154 gold
- SOCKS5: 177 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43271
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
