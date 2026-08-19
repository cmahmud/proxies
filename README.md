# SyndProxy private pool

## Current pool

- Alive now: 1054
- Gold now: 534
- HTTP: 377 alive / 154 gold
- HTTPS: 263 alive / 107 gold
- SOCKS4: 213 alive / 144 gold
- SOCKS5: 201 alive / 129 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19916
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
