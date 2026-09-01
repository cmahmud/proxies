# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 448
- HTTP: 98 alive / 75 gold
- HTTPS: 104 alive / 31 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 189 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47389
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
