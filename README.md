# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 210
- HTTP: 262 alive / 26 gold
- HTTPS: 213 alive / 8 gold
- SOCKS4: 221 alive / 94 gold
- SOCKS5: 242 alive / 82 gold

## Historical pool

- Discovered: 91700
- Ever alive: 8643
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
