# SyndProxy private pool

## Current pool

- Alive now: 1213
- Gold now: 411
- HTTP: 408 alive / 95 gold
- HTTPS: 259 alive / 15 gold
- SOCKS4: 238 alive / 151 gold
- SOCKS5: 308 alive / 150 gold

## Historical pool

- Discovered: 131841
- Ever alive: 21174
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
