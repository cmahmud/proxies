# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 454
- HTTP: 134 alive / 84 gold
- HTTPS: 127 alive / 32 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 196 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46838
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
