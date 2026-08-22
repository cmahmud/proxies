# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 443
- HTTP: 291 alive / 98 gold
- HTTPS: 205 alive / 31 gold
- SOCKS4: 229 alive / 147 gold
- SOCKS5: 274 alive / 167 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31039
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
