# SyndProxy private pool

## Current pool

- Alive now: 1026
- Gold now: 421
- HTTP: 304 alive / 90 gold
- HTTPS: 208 alive / 23 gold
- SOCKS4: 236 alive / 140 gold
- SOCKS5: 278 alive / 168 gold

## Historical pool

- Discovered: 164947
- Ever alive: 32223
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
