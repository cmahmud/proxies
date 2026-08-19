# SyndProxy private pool

## Current pool

- Alive now: 1186
- Gold now: 496
- HTTP: 411 alive / 144 gold
- HTTPS: 297 alive / 91 gold
- SOCKS4: 229 alive / 124 gold
- SOCKS5: 249 alive / 137 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17289
- Ever gold: 661

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
