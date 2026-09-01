# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 466
- HTTP: 133 alive / 96 gold
- HTTPS: 112 alive / 33 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 203 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46315
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
