# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 463
- HTTP: 136 alive / 95 gold
- HTTPS: 131 alive / 31 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 214 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46138
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
