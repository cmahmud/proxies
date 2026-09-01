# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 421
- HTTP: 88 alive / 66 gold
- HTTPS: 107 alive / 28 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 176 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47271
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
