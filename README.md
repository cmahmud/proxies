# SyndProxy private pool

## Current pool

- Alive now: 891
- Gold now: 404
- HTTP: 235 alive / 94 gold
- HTTPS: 161 alive / 22 gold
- SOCKS4: 225 alive / 134 gold
- SOCKS5: 270 alive / 154 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29030
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
