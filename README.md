# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 434
- HTTP: 102 alive / 74 gold
- HTTPS: 98 alive / 24 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 182 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47662
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
