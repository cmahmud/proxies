# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 397
- HTTP: 261 alive / 95 gold
- HTTPS: 211 alive / 31 gold
- SOCKS4: 202 alive / 146 gold
- SOCKS5: 234 alive / 125 gold

## Historical pool

- Discovered: 161010
- Ever alive: 31005
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
