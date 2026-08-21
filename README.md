# SyndProxy private pool

## Current pool

- Alive now: 862
- Gold now: 362
- HTTP: 299 alive / 75 gold
- HTTPS: 173 alive / 19 gold
- SOCKS4: 185 alive / 127 gold
- SOCKS5: 205 alive / 141 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29669
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
