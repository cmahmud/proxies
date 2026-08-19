# SyndProxy private pool

## Current pool

- Alive now: 1115
- Gold now: 376
- HTTP: 368 alive / 91 gold
- HTTPS: 222 alive / 14 gold
- SOCKS4: 234 alive / 136 gold
- SOCKS5: 291 alive / 135 gold

## Historical pool

- Discovered: 131826
- Ever alive: 20995
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
