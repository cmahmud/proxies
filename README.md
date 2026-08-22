# SyndProxy private pool

## Current pool

- Alive now: 835
- Gold now: 378
- HTTP: 265 alive / 82 gold
- HTTPS: 157 alive / 28 gold
- SOCKS4: 205 alive / 137 gold
- SOCKS5: 208 alive / 131 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31595
- Ever gold: 1162

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
