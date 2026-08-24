# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 432
- HTTP: 121 alive / 78 gold
- HTTPS: 88 alive / 24 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34666
- Ever gold: 1257

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
