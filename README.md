# SyndProxy private pool

## Current pool

- Alive now: 831
- Gold now: 401
- HTTP: 252 alive / 91 gold
- HTTPS: 127 alive / 19 gold
- SOCKS4: 216 alive / 151 gold
- SOCKS5: 236 alive / 140 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29244
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
