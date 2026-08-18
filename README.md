# SyndProxy private pool

## Current pool

- Alive now: 930
- Gold now: 279
- HTTP: 344 alive / 37 gold
- HTTPS: 201 alive / 10 gold
- SOCKS4: 221 alive / 140 gold
- SOCKS5: 164 alive / 92 gold

## Historical pool

- Discovered: 102917
- Ever alive: 13932
- Ever gold: 433

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
