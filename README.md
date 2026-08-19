# SyndProxy private pool

## Current pool

- Alive now: 1217
- Gold now: 497
- HTTP: 409 alive / 145 gold
- HTTPS: 342 alive / 92 gold
- SOCKS4: 208 alive / 123 gold
- SOCKS5: 258 alive / 137 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17328
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
