# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 408
- HTTP: 76 alive / 62 gold
- HTTPS: 99 alive / 22 gold
- SOCKS4: 163 alive / 158 gold
- SOCKS5: 173 alive / 166 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47211
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
