# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 407
- HTTP: 86 alive / 61 gold
- HTTPS: 103 alive / 25 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 176 alive / 163 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47213
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
