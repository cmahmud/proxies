# SyndProxy private pool

## Current pool

- Alive now: 785
- Gold now: 397
- HTTP: 203 alive / 87 gold
- HTTPS: 130 alive / 25 gold
- SOCKS4: 217 alive / 135 gold
- SOCKS5: 235 alive / 150 gold

## Historical pool

- Discovered: 154727
- Ever alive: 29159
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
