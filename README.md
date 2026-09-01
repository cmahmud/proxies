# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 457
- HTTP: 124 alive / 85 gold
- HTTPS: 104 alive / 39 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46975
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
