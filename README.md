# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 463
- HTTP: 139 alive / 95 gold
- HTTPS: 131 alive / 31 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 215 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46139
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
