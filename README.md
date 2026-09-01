# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 425
- HTTP: 90 alive / 69 gold
- HTTPS: 107 alive / 31 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47292
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
