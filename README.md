# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 402
- HTTP: 100 alive / 61 gold
- HTTPS: 81 alive / 14 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 197 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39282
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
