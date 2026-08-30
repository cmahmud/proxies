# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 439
- HTTP: 120 alive / 82 gold
- HTTPS: 61 alive / 26 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43689
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
