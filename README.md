# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 411
- HTTP: 97 alive / 61 gold
- HTTPS: 89 alive / 23 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42722
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
