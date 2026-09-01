# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 416
- HTTP: 88 alive / 65 gold
- HTTPS: 98 alive / 25 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 178 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47246
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
