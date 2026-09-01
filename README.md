# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 423
- HTTP: 86 alive / 67 gold
- HTTPS: 105 alive / 28 gold
- SOCKS4: 178 alive / 158 gold
- SOCKS5: 177 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47271
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
