# SyndProxy private pool

## Current pool

- Alive now: 1060
- Gold now: 391
- HTTP: 353 alive / 88 gold
- HTTPS: 219 alive / 29 gold
- SOCKS4: 249 alive / 147 gold
- SOCKS5: 239 alive / 127 gold

## Historical pool

- Discovered: 160990
- Ever alive: 30881
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
