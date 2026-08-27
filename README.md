# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 405
- HTTP: 90 alive / 64 gold
- HTTPS: 80 alive / 18 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 177 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41745
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
