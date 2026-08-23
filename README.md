# SyndProxy validated proxy pool

## Current pool

- Alive now: 708
- Gold now: 101
- HTTP: 233 alive / 30 gold
- HTTPS: 96 alive / 2 gold
- SOCKS4: 109 alive / 0 gold
- SOCKS5: 270 alive / 69 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32670
- Ever gold: 1193

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
