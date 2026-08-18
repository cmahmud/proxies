# SyndProxy private pool

## Current pool

- Alive now: 765
- Gold now: 271
- HTTP: 208 alive / 22 gold
- HTTPS: 134 alive / 2 gold
- SOCKS4: 226 alive / 136 gold
- SOCKS5: 197 alive / 111 gold

## Historical pool

- Discovered: 99098
- Ever alive: 11476
- Ever gold: 388

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
