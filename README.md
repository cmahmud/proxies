# SyndProxy private pool

## Current pool

- Alive now: 1004
- Gold now: 301
- HTTP: 394 alive / 29 gold
- HTTPS: 193 alive / 5 gold
- SOCKS4: 209 alive / 141 gold
- SOCKS5: 208 alive / 126 gold

## Historical pool

- Discovered: 102848
- Ever alive: 13402
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
