# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 449
- HTTP: 304 alive / 105 gold
- HTTPS: 208 alive / 35 gold
- SOCKS4: 193 alive / 148 gold
- SOCKS5: 271 alive / 161 gold

## Historical pool

- Discovered: 153732
- Ever alive: 28678
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
