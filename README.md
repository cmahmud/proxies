# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 210
- HTTP: 268 alive / 26 gold
- HTTPS: 187 alive / 8 gold
- SOCKS4: 218 alive / 94 gold
- SOCKS5: 241 alive / 82 gold

## Historical pool

- Discovered: 91700
- Ever alive: 8643
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
