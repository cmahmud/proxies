# SyndProxy private pool

## Current pool

- Alive now: 1216
- Gold now: 405
- HTTP: 400 alive / 87 gold
- HTTPS: 257 alive / 17 gold
- SOCKS4: 242 alive / 148 gold
- SOCKS5: 317 alive / 153 gold

## Historical pool

- Discovered: 134540
- Ever alive: 21977
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
