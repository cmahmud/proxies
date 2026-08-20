# SyndProxy private pool

## Current pool

- Alive now: 882
- Gold now: 412
- HTTP: 243 alive / 90 gold
- HTTPS: 215 alive / 19 gold
- SOCKS4: 208 alive / 152 gold
- SOCKS5: 216 alive / 151 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27558
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
