# SyndProxy private pool

## Current pool

- Alive now: 647
- Gold now: 258
- HTTP: 170 alive / 32 gold
- HTTPS: 82 alive / 7 gold
- SOCKS4: 196 alive / 132 gold
- SOCKS5: 199 alive / 87 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9110
- Ever gold: 363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
