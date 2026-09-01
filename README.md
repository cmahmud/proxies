# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 465
- HTTP: 131 alive / 88 gold
- HTTPS: 101 alive / 40 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46970
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
