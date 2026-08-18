# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 345
- HTTP: 310 alive / 49 gold
- HTTPS: 242 alive / 14 gold
- SOCKS4: 249 alive / 144 gold
- SOCKS5: 234 alive / 138 gold

## Historical pool

- Discovered: 107145
- Ever alive: 15100
- Ever gold: 479

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
