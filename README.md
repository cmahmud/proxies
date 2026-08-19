# SyndProxy private pool

## Current pool

- Alive now: 1266
- Gold now: 418
- HTTP: 413 alive / 98 gold
- HTTPS: 279 alive / 18 gold
- SOCKS4: 252 alive / 142 gold
- SOCKS5: 322 alive / 160 gold

## Historical pool

- Discovered: 131823
- Ever alive: 20967
- Ever gold: 877

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
