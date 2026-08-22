# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 414
- HTTP: 308 alive / 89 gold
- HTTPS: 234 alive / 27 gold
- SOCKS4: 197 alive / 128 gold
- SOCKS5: 255 alive / 170 gold

## Historical pool

- Discovered: 161925
- Ever alive: 31185
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
