# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 386
- HTTP: 269 alive / 80 gold
- HTTPS: 197 alive / 27 gold
- SOCKS4: 197 alive / 123 gold
- SOCKS5: 249 alive / 156 gold

## Historical pool

- Discovered: 164916
- Ever alive: 32137
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
