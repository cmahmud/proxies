# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 399
- HTTP: 286 alive / 89 gold
- HTTPS: 154 alive / 24 gold
- SOCKS4: 216 alive / 146 gold
- SOCKS5: 226 alive / 140 gold

## Historical pool

- Discovered: 155800
- Ever alive: 29383
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
