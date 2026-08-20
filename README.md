# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 369
- HTTP: 243 alive / 66 gold
- HTTPS: 183 alive / 14 gold
- SOCKS4: 205 alive / 151 gold
- SOCKS5: 205 alive / 138 gold

## Historical pool

- Discovered: 147685
- Ever alive: 25901
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
