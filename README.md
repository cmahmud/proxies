# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 447
- HTTP: 142 alive / 80 gold
- HTTPS: 117 alive / 28 gold
- SOCKS4: 189 alive / 165 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47632
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
