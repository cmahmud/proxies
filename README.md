# SyndProxy private pool

## Current pool

- Alive now: 897
- Gold now: 425
- HTTP: 247 alive / 87 gold
- HTTPS: 170 alive / 30 gold
- SOCKS4: 216 alive / 149 gold
- SOCKS5: 264 alive / 159 gold

## Historical pool

- Discovered: 153852
- Ever alive: 28891
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
