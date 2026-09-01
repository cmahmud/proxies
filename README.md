# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 474
- HTTP: 133 alive / 95 gold
- HTTPS: 123 alive / 38 gold
- SOCKS4: 184 alive / 162 gold
- SOCKS5: 194 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46348
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
