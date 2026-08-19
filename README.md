# SyndProxy private pool

## Current pool

- Alive now: 1114
- Gold now: 539
- HTTP: 408 alive / 156 gold
- HTTPS: 268 alive / 89 gold
- SOCKS4: 230 alive / 160 gold
- SOCKS5: 208 alive / 134 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18224
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
