# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 405
- HTTP: 83 alive / 60 gold
- HTTPS: 82 alive / 20 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42691
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
