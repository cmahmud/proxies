# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 423
- HTTP: 291 alive / 84 gold
- HTTPS: 213 alive / 27 gold
- SOCKS4: 227 alive / 151 gold
- SOCKS5: 254 alive / 161 gold

## Historical pool

- Discovered: 163873
- Ever alive: 31999
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
