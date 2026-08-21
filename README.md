# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 400
- HTTP: 401 alive / 98 gold
- HTTPS: 250 alive / 28 gold
- SOCKS4: 225 alive / 151 gold
- SOCKS5: 205 alive / 123 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30308
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
