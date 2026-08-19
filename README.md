# SyndProxy private pool

## Current pool

- Alive now: 1268
- Gold now: 533
- HTTP: 463 alive / 183 gold
- HTTPS: 338 alive / 60 gold
- SOCKS4: 220 alive / 123 gold
- SOCKS5: 247 alive / 167 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19659
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
