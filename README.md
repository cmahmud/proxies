# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 384
- HTTP: 333 alive / 98 gold
- HTTPS: 231 alive / 22 gold
- SOCKS4: 228 alive / 130 gold
- SOCKS5: 246 alive / 134 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25071
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
