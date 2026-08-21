# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 410
- HTTP: 351 alive / 95 gold
- HTTPS: 241 alive / 32 gold
- SOCKS4: 216 alive / 151 gold
- SOCKS5: 228 alive / 132 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30965
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
