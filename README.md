# SyndProxy private pool

## Current pool

- Alive now: 1312
- Gold now: 528
- HTTP: 498 alive / 185 gold
- HTTPS: 342 alive / 57 gold
- SOCKS4: 221 alive / 123 gold
- SOCKS5: 251 alive / 163 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19656
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
