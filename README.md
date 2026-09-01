# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 458
- HTTP: 133 alive / 86 gold
- HTTPS: 139 alive / 34 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46694
- Ever gold: 1446

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
