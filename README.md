# SyndProxy private pool

## Current pool

- Alive now: 949
- Gold now: 401
- HTTP: 342 alive / 91 gold
- HTTPS: 157 alive / 24 gold
- SOCKS4: 219 alive / 146 gold
- SOCKS5: 231 alive / 140 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29394
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
