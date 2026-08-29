# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 401
- HTTP: 101 alive / 67 gold
- HTTPS: 54 alive / 23 gold
- SOCKS4: 157 alive / 153 gold
- SOCKS5: 166 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43651
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
