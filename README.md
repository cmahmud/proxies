# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 408
- HTTP: 81 alive / 62 gold
- HTTPS: 94 alive / 23 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47214
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
