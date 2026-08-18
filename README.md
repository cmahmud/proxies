# SyndProxy private pool

## Current pool

- Alive now: 681
- Gold now: 230
- HTTP: 236 alive / 30 gold
- HTTPS: 75 alive / 8 gold
- SOCKS4: 167 alive / 108 gold
- SOCKS5: 203 alive / 84 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8770
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
