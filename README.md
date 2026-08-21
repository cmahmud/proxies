# SyndProxy private pool

## Current pool

- Alive now: 957
- Gold now: 411
- HTTP: 278 alive / 94 gold
- HTTPS: 215 alive / 25 gold
- SOCKS4: 219 alive / 144 gold
- SOCKS5: 245 alive / 148 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29086
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
