# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 427
- HTTP: 104 alive / 72 gold
- HTTPS: 71 alive / 27 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47025
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
