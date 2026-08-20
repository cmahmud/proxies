# SyndProxy private pool

## Current pool

- Alive now: 791
- Gold now: 381
- HTTP: 178 alive / 75 gold
- HTTPS: 201 alive / 22 gold
- SOCKS4: 205 alive / 149 gold
- SOCKS5: 207 alive / 135 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26144
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
