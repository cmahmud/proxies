# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 458
- HTTP: 122 alive / 87 gold
- HTTPS: 130 alive / 33 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46811
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
