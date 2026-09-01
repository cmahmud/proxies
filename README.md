# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 455
- HTTP: 136 alive / 84 gold
- HTTPS: 124 alive / 33 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46840
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
