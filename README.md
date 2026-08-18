# SyndProxy private pool

## Current pool

- Alive now: 729
- Gold now: 272
- HTTP: 187 alive / 22 gold
- HTTPS: 124 alive / 2 gold
- SOCKS4: 223 alive / 137 gold
- SOCKS5: 195 alive / 111 gold

## Historical pool

- Discovered: 99103
- Ever alive: 11476
- Ever gold: 388

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
