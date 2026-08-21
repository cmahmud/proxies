# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 402
- HTTP: 277 alive / 74 gold
- HTTPS: 160 alive / 24 gold
- SOCKS4: 231 alive / 156 gold
- SOCKS5: 245 alive / 148 gold

## Historical pool

- Discovered: 156747
- Ever alive: 29598
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
