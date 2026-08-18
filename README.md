# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 252
- HTTP: 221 alive / 29 gold
- HTTPS: 134 alive / 7 gold
- SOCKS4: 233 alive / 124 gold
- SOCKS5: 233 alive / 92 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9082
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
