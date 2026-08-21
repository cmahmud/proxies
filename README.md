# SyndProxy private pool

## Current pool

- Alive now: 968
- Gold now: 411
- HTTP: 301 alive / 102 gold
- HTTPS: 214 alive / 29 gold
- SOCKS4: 225 alive / 156 gold
- SOCKS5: 228 alive / 124 gold

## Historical pool

- Discovered: 160353
- Ever alive: 30811
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
