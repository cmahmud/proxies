# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 413
- HTTP: 98 alive / 74 gold
- HTTPS: 120 alive / 19 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 177 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42017
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
