# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 499
- HTTP: 329 alive / 133 gold
- HTTPS: 259 alive / 83 gold
- SOCKS4: 237 alive / 150 gold
- SOCKS5: 207 alive / 133 gold

## Historical pool

- Discovered: 119696
- Ever alive: 17898
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
