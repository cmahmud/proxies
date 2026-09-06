# SyndProxy validated proxy pool

## Current pool

- Alive now: 388
- Gold now: 307
- HTTP: 73 alive / 47 gold
- HTTPS: 29 alive / 7 gold
- SOCKS4: 144 alive / 134 gold
- SOCKS5: 142 alive / 119 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48326
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
