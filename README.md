# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 449
- HTTP: 125 alive / 81 gold
- HTTPS: 121 alive / 33 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46844
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
