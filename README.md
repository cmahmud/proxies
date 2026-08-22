# SyndProxy private pool

## Current pool

- Alive now: 949
- Gold now: 422
- HTTP: 277 alive / 93 gold
- HTTPS: 220 alive / 26 gold
- SOCKS4: 209 alive / 144 gold
- SOCKS5: 243 alive / 159 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31839
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
