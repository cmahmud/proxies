# SyndProxy private pool

## Current pool

- Alive now: 1280
- Gold now: 536
- HTTP: 473 alive / 180 gold
- HTTPS: 337 alive / 59 gold
- SOCKS4: 224 alive / 140 gold
- SOCKS5: 246 alive / 157 gold

## Historical pool

- Discovered: 125594
- Ever alive: 19571
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
