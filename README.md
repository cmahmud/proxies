# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 459
- HTTP: 127 alive / 85 gold
- HTTPS: 116 alive / 35 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46797
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
