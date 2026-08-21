# SyndProxy private pool

## Current pool

- Alive now: 984
- Gold now: 427
- HTTP: 286 alive / 89 gold
- HTTPS: 235 alive / 32 gold
- SOCKS4: 218 alive / 154 gold
- SOCKS5: 245 alive / 152 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30238
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
