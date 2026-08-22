# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 380
- HTTP: 323 alive / 90 gold
- HTTPS: 271 alive / 26 gold
- SOCKS4: 155 alive / 102 gold
- SOCKS5: 258 alive / 162 gold

## Historical pool

- Discovered: 166625
- Ever alive: 32459
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
