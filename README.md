# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 469
- HTTP: 131 alive / 94 gold
- HTTPS: 120 alive / 39 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 197 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46366
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
