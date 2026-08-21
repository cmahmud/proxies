# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 403
- HTTP: 217 alive / 90 gold
- HTTPS: 145 alive / 25 gold
- SOCKS4: 213 alive / 136 gold
- SOCKS5: 242 alive / 152 gold

## Historical pool

- Discovered: 154731
- Ever alive: 29172
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
