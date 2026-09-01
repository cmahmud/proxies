# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 453
- HTTP: 124 alive / 88 gold
- HTTPS: 117 alive / 28 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 188 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46735
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
