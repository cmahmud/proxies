# SyndProxy private pool

## Current pool

- Alive now: 949
- Gold now: 340
- HTTP: 335 alive / 58 gold
- HTTPS: 197 alive / 14 gold
- SOCKS4: 217 alive / 134 gold
- SOCKS5: 200 alive / 134 gold

## Historical pool

- Discovered: 129235
- Ever alive: 20040
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
