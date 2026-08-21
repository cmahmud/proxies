# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 419
- HTTP: 258 alive / 92 gold
- HTTPS: 166 alive / 25 gold
- SOCKS4: 221 alive / 139 gold
- SOCKS5: 267 alive / 163 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29033
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
