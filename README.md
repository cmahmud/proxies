# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 422
- HTTP: 321 alive / 86 gold
- HTTPS: 212 alive / 23 gold
- SOCKS4: 239 alive / 142 gold
- SOCKS5: 292 alive / 171 gold

## Historical pool

- Discovered: 164946
- Ever alive: 32215
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
