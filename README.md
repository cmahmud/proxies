# SyndProxy private pool

## Current pool

- Alive now: 922
- Gold now: 404
- HTTP: 258 alive / 76 gold
- HTTPS: 193 alive / 21 gold
- SOCKS4: 224 alive / 146 gold
- SOCKS5: 247 alive / 161 gold

## Historical pool

- Discovered: 155790
- Ever alive: 29330
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
