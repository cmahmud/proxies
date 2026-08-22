# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 404
- HTTP: 324 alive / 77 gold
- HTTPS: 220 alive / 18 gold
- SOCKS4: 223 alive / 149 gold
- SOCKS5: 247 alive / 160 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32295
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
