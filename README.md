# SyndProxy private pool

## Current pool

- Alive now: 757
- Gold now: 411
- HTTP: 180 alive / 85 gold
- HTTPS: 148 alive / 24 gold
- SOCKS4: 206 alive / 156 gold
- SOCKS5: 223 alive / 146 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26976
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
