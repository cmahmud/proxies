# SyndProxy private pool

## Current pool

- Alive now: 666
- Gold now: 377
- HTTP: 161 alive / 70 gold
- HTTPS: 88 alive / 13 gold
- SOCKS4: 196 alive / 137 gold
- SOCKS5: 221 alive / 157 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25794
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
