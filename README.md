# SyndProxy private pool

## Current pool

- Alive now: 963
- Gold now: 338
- HTTP: 365 alive / 58 gold
- HTTPS: 186 alive / 14 gold
- SOCKS4: 209 alive / 132 gold
- SOCKS5: 203 alive / 134 gold

## Historical pool

- Discovered: 129235
- Ever alive: 20040
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
