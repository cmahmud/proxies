# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 405
- HTTP: 262 alive / 91 gold
- HTTPS: 179 alive / 19 gold
- SOCKS4: 215 alive / 152 gold
- SOCKS5: 236 alive / 143 gold

## Historical pool

- Discovered: 155696
- Ever alive: 29275
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
