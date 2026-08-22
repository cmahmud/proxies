# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 443
- HTTP: 309 alive / 97 gold
- HTTPS: 241 alive / 32 gold
- SOCKS4: 216 alive / 147 gold
- SOCKS5: 275 alive / 167 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31062
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
