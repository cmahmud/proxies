# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 396
- HTTP: 94 alive / 68 gold
- HTTPS: 73 alive / 15 gold
- SOCKS4: 162 alive / 152 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43261
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
