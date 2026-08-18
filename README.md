# SyndProxy private pool

## Current pool

- Alive now: 818
- Gold now: 217
- HTTP: 258 alive / 29 gold
- HTTPS: 136 alive / 10 gold
- SOCKS4: 204 alive / 97 gold
- SOCKS5: 220 alive / 81 gold

## Historical pool

- Discovered: 86777
- Ever alive: 7959
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
