# SyndProxy private pool

## Current pool

- Alive now: 726
- Gold now: 390
- HTTP: 177 alive / 86 gold
- HTTPS: 129 alive / 17 gold
- SOCKS4: 205 alive / 136 gold
- SOCKS5: 215 alive / 151 gold

## Historical pool

- Discovered: 154732
- Ever alive: 29184
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
