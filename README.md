# SyndProxy validated proxy pool

## Current pool

- Alive now: 657
- Gold now: 408
- HTTP: 106 alive / 67 gold
- HTTPS: 179 alive / 19 gold
- SOCKS4: 177 alive / 157 gold
- SOCKS5: 195 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40614
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
