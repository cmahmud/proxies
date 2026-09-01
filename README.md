# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 416
- HTTP: 96 alive / 64 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 178 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47085
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
