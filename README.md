# SyndProxy private pool

## Current pool

- Alive now: 1127
- Gold now: 443
- HTTP: 374 alive / 110 gold
- HTTPS: 274 alive / 34 gold
- SOCKS4: 209 alive / 143 gold
- SOCKS5: 270 alive / 156 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28652
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
