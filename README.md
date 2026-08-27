# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 399
- HTTP: 98 alive / 58 gold
- HTTPS: 56 alive / 21 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 185 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41711
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
