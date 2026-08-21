# SyndProxy private pool

## Current pool

- Alive now: 766
- Gold now: 403
- HTTP: 219 alive / 85 gold
- HTTPS: 113 alive / 20 gold
- SOCKS4: 211 alive / 147 gold
- SOCKS5: 223 alive / 151 gold

## Historical pool

- Discovered: 155785
- Ever alive: 29292
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
