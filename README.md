# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 382
- HTTP: 87 alive / 66 gold
- HTTPS: 92 alive / 13 gold
- SOCKS4: 159 alive / 149 gold
- SOCKS5: 179 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43253
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
