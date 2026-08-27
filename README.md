# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 411
- HTTP: 105 alive / 70 gold
- HTTPS: 163 alive / 17 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40956
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
