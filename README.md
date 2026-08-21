# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 395
- HTTP: 200 alive / 85 gold
- HTTPS: 135 alive / 26 gold
- SOCKS4: 213 alive / 135 gold
- SOCKS5: 235 alive / 149 gold

## Historical pool

- Discovered: 154727
- Ever alive: 29165
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
