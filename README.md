# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 459
- HTTP: 126 alive / 85 gold
- HTTPS: 118 alive / 34 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 189 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46795
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
