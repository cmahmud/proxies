# SyndProxy private pool

## Current pool

- Alive now: 947
- Gold now: 390
- HTTP: 278 alive / 77 gold
- HTTPS: 213 alive / 23 gold
- SOCKS4: 219 alive / 144 gold
- SOCKS5: 237 alive / 146 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29578
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
