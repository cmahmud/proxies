# SyndProxy private pool

## Current pool

- Alive now: 984
- Gold now: 400
- HTTP: 307 alive / 95 gold
- HTTPS: 239 alive / 34 gold
- SOCKS4: 216 alive / 152 gold
- SOCKS5: 222 alive / 119 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30294
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
