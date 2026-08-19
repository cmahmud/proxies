# SyndProxy private pool

## Current pool

- Alive now: 1164
- Gold now: 428
- HTTP: 416 alive / 124 gold
- HTTPS: 278 alive / 42 gold
- SOCKS4: 219 alive / 124 gold
- SOCKS5: 251 alive / 138 gold

## Historical pool

- Discovered: 117088
- Ever alive: 17128
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
