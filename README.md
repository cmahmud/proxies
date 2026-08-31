# SyndProxy validated proxy pool

## Current pool

- Alive now: 710
- Gold now: 460
- HTTP: 153 alive / 95 gold
- HTTPS: 129 alive / 29 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 246 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46263
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
