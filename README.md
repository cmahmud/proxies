# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 364
- HTTP: 83 alive / 53 gold
- HTTPS: 67 alive / 16 gold
- SOCKS4: 161 alive / 152 gold
- SOCKS5: 167 alive / 143 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43467
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
