# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 219
- HTTP: 269 alive / 32 gold
- HTTPS: 140 alive / 9 gold
- SOCKS4: 209 alive / 110 gold
- SOCKS5: 203 alive / 68 gold

## Historical pool

- Discovered: 94321
- Ever alive: 9327
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
