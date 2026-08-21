# SyndProxy private pool

## Current pool

- Alive now: 725
- Gold now: 401
- HTTP: 184 alive / 87 gold
- HTTPS: 122 alive / 19 gold
- SOCKS4: 212 alive / 143 gold
- SOCKS5: 207 alive / 152 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27731
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
