# SyndProxy private pool

## Current pool

- Alive now: 1078
- Gold now: 403
- HTTP: 393 alive / 100 gold
- HTTPS: 258 alive / 31 gold
- SOCKS4: 218 alive / 151 gold
- SOCKS5: 209 alive / 121 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30303
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
