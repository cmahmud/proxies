# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 394
- HTTP: 83 alive / 65 gold
- HTTPS: 75 alive / 14 gold
- SOCKS4: 162 alive / 158 gold
- SOCKS5: 166 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43365
- Ever gold: 1370

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
