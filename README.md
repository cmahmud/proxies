# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 448
- HTTP: 127 alive / 81 gold
- HTTPS: 124 alive / 33 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46844
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
