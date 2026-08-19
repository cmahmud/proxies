# SyndProxy private pool

## Current pool

- Alive now: 1010
- Gold now: 361
- HTTP: 296 alive / 71 gold
- HTTPS: 244 alive / 18 gold
- SOCKS4: 250 alive / 152 gold
- SOCKS5: 220 alive / 120 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15935
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
