# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 439
- HTTP: 311 alive / 94 gold
- HTTPS: 237 alive / 34 gold
- SOCKS4: 223 alive / 155 gold
- SOCKS5: 251 alive / 156 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30247
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
