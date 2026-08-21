# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 423
- HTTP: 363 alive / 88 gold
- HTTPS: 211 alive / 26 gold
- SOCKS4: 213 alive / 152 gold
- SOCKS5: 243 alive / 157 gold

## Historical pool

- Discovered: 158911
- Ever alive: 30093
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
