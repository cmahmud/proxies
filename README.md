# SyndProxy private pool

## Current pool

- Alive now: 1295
- Gold now: 533
- HTTP: 487 alive / 184 gold
- HTTPS: 342 alive / 62 gold
- SOCKS4: 219 alive / 124 gold
- SOCKS5: 247 alive / 163 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19656
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
