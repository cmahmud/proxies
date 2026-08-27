# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 408
- HTTP: 90 alive / 61 gold
- HTTPS: 54 alive / 23 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41716
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
