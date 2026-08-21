# SyndProxy private pool

## Current pool

- Alive now: 900
- Gold now: 408
- HTTP: 277 alive / 83 gold
- HTTPS: 161 alive / 25 gold
- SOCKS4: 226 alive / 152 gold
- SOCKS5: 236 alive / 148 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29594
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
