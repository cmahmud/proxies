# SyndProxy private pool

## Current pool

- Alive now: 1255
- Gold now: 534
- HTTP: 452 alive / 183 gold
- HTTPS: 338 alive / 60 gold
- SOCKS4: 213 alive / 123 gold
- SOCKS5: 252 alive / 168 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19662
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
