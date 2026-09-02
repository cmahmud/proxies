# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 434
- HTTP: 102 alive / 74 gold
- HTTPS: 101 alive / 24 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 184 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47663
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
