# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 386
- HTTP: 99 alive / 63 gold
- HTTPS: 101 alive / 13 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 179 alive / 148 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43038
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
