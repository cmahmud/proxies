# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 364
- HTTP: 248 alive / 92 gold
- HTTPS: 139 alive / 29 gold
- SOCKS4: 181 alive / 105 gold
- SOCKS5: 226 alive / 138 gold

## Historical pool

- Discovered: 167356
- Ever alive: 32558
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
