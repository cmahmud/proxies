# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 395
- HTTP: 324 alive / 91 gold
- HTTPS: 229 alive / 30 gold
- SOCKS4: 238 alive / 143 gold
- SOCKS5: 250 alive / 131 gold

## Historical pool

- Discovered: 160990
- Ever alive: 30891
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
