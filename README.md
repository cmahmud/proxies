# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 468
- HTTP: 133 alive / 96 gold
- HTTPS: 126 alive / 34 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 222 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46042
- Ever gold: 1439

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
