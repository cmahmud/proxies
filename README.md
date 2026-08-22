# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 395
- HTTP: 207 alive / 98 gold
- HTTPS: 207 alive / 24 gold
- SOCKS4: 193 alive / 127 gold
- SOCKS5: 215 alive / 146 gold

## Historical pool

- Discovered: 162001
- Ever alive: 31370
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
