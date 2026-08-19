# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 485
- HTTP: 364 alive / 134 gold
- HTTPS: 258 alive / 78 gold
- SOCKS4: 208 alive / 123 gold
- SOCKS5: 229 alive / 150 gold

## Historical pool

- Discovered: 119695
- Ever alive: 17866
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
