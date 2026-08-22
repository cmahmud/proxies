# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 421
- HTTP: 323 alive / 89 gold
- HTTPS: 218 alive / 29 gold
- SOCKS4: 239 alive / 147 gold
- SOCKS5: 258 alive / 156 gold

## Historical pool

- Discovered: 164927
- Ever alive: 32165
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
