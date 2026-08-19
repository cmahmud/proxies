# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 526
- HTTP: 415 alive / 185 gold
- HTTPS: 258 alive / 112 gold
- SOCKS4: 208 alive / 111 gold
- SOCKS5: 202 alive / 118 gold

## Historical pool

- Discovered: 124845
- Ever alive: 19386
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
