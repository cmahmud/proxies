# SyndProxy private pool

## Current pool

- Alive now: 885
- Gold now: 379
- HTTP: 282 alive / 83 gold
- HTTPS: 180 alive / 26 gold
- SOCKS4: 211 alive / 140 gold
- SOCKS5: 212 alive / 130 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31596
- Ever gold: 1162

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
