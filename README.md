# SyndProxy private pool

## Current pool

- Alive now: 704
- Gold now: 373
- HTTP: 169 alive / 69 gold
- HTTPS: 149 alive / 19 gold
- SOCKS4: 196 alive / 148 gold
- SOCKS5: 190 alive / 137 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26206
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
