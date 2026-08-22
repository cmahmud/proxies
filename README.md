# SyndProxy private pool

## Current pool

- Alive now: 886
- Gold now: 388
- HTTP: 267 alive / 88 gold
- HTTPS: 178 alive / 21 gold
- SOCKS4: 192 alive / 113 gold
- SOCKS5: 249 alive / 166 gold

## Historical pool

- Discovered: 166612
- Ever alive: 32436
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
