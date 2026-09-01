# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 460
- HTTP: 124 alive / 83 gold
- HTTPS: 130 alive / 37 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 195 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46762
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
