# SyndProxy private pool

## Current pool

- Alive now: 869
- Gold now: 404
- HTTP: 219 alive / 94 gold
- HTTPS: 158 alive / 22 gold
- SOCKS4: 223 alive / 134 gold
- SOCKS5: 269 alive / 154 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29030
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
