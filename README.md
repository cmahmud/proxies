# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 449
- HTTP: 99 alive / 76 gold
- HTTPS: 110 alive / 31 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 188 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47389
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
