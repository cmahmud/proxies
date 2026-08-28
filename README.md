# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 383
- HTTP: 90 alive / 65 gold
- HTTPS: 87 alive / 12 gold
- SOCKS4: 158 alive / 148 gold
- SOCKS5: 179 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43236
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
