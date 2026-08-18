# SyndProxy private pool

## Current pool

- Alive now: 688
- Gold now: 252
- HTTP: 159 alive / 29 gold
- HTTPS: 92 alive / 6 gold
- SOCKS4: 229 alive / 124 gold
- SOCKS5: 208 alive / 93 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9108
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
