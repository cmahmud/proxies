# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 460
- HTTP: 133 alive / 89 gold
- HTTPS: 85 alive / 35 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46983
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
