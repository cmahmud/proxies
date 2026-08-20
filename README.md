# SyndProxy private pool

## Current pool

- Alive now: 748
- Gold now: 408
- HTTP: 192 alive / 89 gold
- HTTPS: 157 alive / 21 gold
- SOCKS4: 190 alive / 144 gold
- SOCKS5: 209 alive / 154 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27409
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
