# SyndProxy private pool

## Current pool

- Alive now: 963
- Gold now: 412
- HTTP: 295 alive / 96 gold
- HTTPS: 189 alive / 27 gold
- SOCKS4: 213 alive / 139 gold
- SOCKS5: 266 alive / 150 gold

## Historical pool

- Discovered: 154713
- Ever alive: 29011
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
