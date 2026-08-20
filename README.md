# SyndProxy private pool

## Current pool

- Alive now: 765
- Gold now: 400
- HTTP: 217 alive / 85 gold
- HTTPS: 129 alive / 20 gold
- SOCKS4: 205 alive / 142 gold
- SOCKS5: 214 alive / 153 gold

## Historical pool

- Discovered: 147690
- Ever alive: 25990
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
