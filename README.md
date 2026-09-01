# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 463
- HTTP: 122 alive / 86 gold
- HTTPS: 98 alive / 42 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46973
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
