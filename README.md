# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 387
- HTTP: 93 alive / 66 gold
- HTTPS: 88 alive / 11 gold
- SOCKS4: 156 alive / 152 gold
- SOCKS5: 179 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43241
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
