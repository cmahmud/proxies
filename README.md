# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 364
- HTTP: 317 alive / 77 gold
- HTTPS: 175 alive / 18 gold
- SOCKS4: 196 alive / 128 gold
- SOCKS5: 223 alive / 141 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29669
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
