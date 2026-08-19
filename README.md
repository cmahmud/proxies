# SyndProxy private pool

## Current pool

- Alive now: 1002
- Gold now: 489
- HTTP: 352 alive / 130 gold
- HTTPS: 262 alive / 105 gold
- SOCKS4: 192 alive / 125 gold
- SOCKS5: 196 alive / 129 gold

## Historical pool

- Discovered: 127417
- Ever alive: 19967
- Ever gold: 861

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
