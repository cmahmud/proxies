# SyndProxy private pool

## Current pool

- Alive now: 1129
- Gold now: 269
- HTTP: 440 alive / 25 gold
- HTTPS: 230 alive / 5 gold
- SOCKS4: 225 alive / 122 gold
- SOCKS5: 234 alive / 117 gold

## Historical pool

- Discovered: 102835
- Ever alive: 13053
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
