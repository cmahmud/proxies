# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 368
- HTTP: 297 alive / 77 gold
- HTTPS: 209 alive / 25 gold
- SOCKS4: 215 alive / 124 gold
- SOCKS5: 250 alive / 142 gold

## Historical pool

- Discovered: 165819
- Ever alive: 32331
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
