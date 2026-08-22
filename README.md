# SyndProxy private pool

## Current pool

- Alive now: 787
- Gold now: 399
- HTTP: 212 alive / 92 gold
- HTTPS: 161 alive / 28 gold
- SOCKS4: 188 alive / 127 gold
- SOCKS5: 226 alive / 152 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31383
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
