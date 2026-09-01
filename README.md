# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 453
- HTTP: 135 alive / 84 gold
- HTTPS: 105 alive / 34 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46990
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
