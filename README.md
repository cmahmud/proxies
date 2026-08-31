# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 465
- HTTP: 120 alive / 91 gold
- HTTPS: 119 alive / 33 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 218 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45966
- Ever gold: 1438

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
