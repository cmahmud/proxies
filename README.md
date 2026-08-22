# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 394
- HTTP: 241 alive / 85 gold
- HTTPS: 208 alive / 23 gold
- SOCKS4: 220 alive / 129 gold
- SOCKS5: 243 alive / 157 gold

## Historical pool

- Discovered: 164909
- Ever alive: 32121
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
