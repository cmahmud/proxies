# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 439
- HTTP: 100 alive / 81 gold
- HTTPS: 45 alive / 27 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43685
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
