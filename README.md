# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 259
- HTTP: 287 alive / 27 gold
- HTTPS: 137 alive / 3 gold
- SOCKS4: 228 alive / 119 gold
- SOCKS5: 230 alive / 110 gold

## Historical pool

- Discovered: 99142
- Ever alive: 12046
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
