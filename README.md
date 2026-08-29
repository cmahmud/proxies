# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 366
- HTTP: 82 alive / 54 gold
- HTTPS: 73 alive / 17 gold
- SOCKS4: 161 alive / 152 gold
- SOCKS5: 168 alive / 143 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43466
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
