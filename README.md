# SyndProxy private pool

## Current pool

- Alive now: 787
- Gold now: 404
- HTTP: 206 alive / 93 gold
- HTTPS: 143 alive / 23 gold
- SOCKS4: 203 alive / 136 gold
- SOCKS5: 235 alive / 152 gold

## Historical pool

- Discovered: 154732
- Ever alive: 29172
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
