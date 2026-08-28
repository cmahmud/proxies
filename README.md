# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 408
- HTTP: 82 alive / 60 gold
- HTTPS: 66 alive / 20 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 194 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42729
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
