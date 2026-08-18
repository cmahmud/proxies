# SyndProxy private pool

## Current pool

- Alive now: 941
- Gold now: 242
- HTTP: 351 alive / 39 gold
- HTTPS: 145 alive / 7 gold
- SOCKS4: 232 alive / 131 gold
- SOCKS5: 213 alive / 65 gold

## Historical pool

- Discovered: 94342
- Ever alive: 9643
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
