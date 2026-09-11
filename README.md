# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 422
- HTTP: 94 alive / 67 gold
- HTTPS: 48 alive / 27 gold
- SOCKS4: 188 alive / 166 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49044
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
