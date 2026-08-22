# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 421
- HTTP: 295 alive / 83 gold
- HTTPS: 199 alive / 25 gold
- SOCKS4: 240 alive / 152 gold
- SOCKS5: 260 alive / 161 gold

## Historical pool

- Discovered: 163873
- Ever alive: 32001
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
