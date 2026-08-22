# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 370
- HTTP: 286 alive / 77 gold
- HTTPS: 215 alive / 25 gold
- SOCKS4: 221 alive / 124 gold
- SOCKS5: 249 alive / 144 gold

## Historical pool

- Discovered: 165816
- Ever alive: 32326
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
