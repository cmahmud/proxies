# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 472
- HTTP: 131 alive / 94 gold
- HTTPS: 119 alive / 37 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 192 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46350
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
