# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 429
- HTTP: 329 alive / 94 gold
- HTTPS: 219 alive / 23 gold
- SOCKS4: 211 alive / 152 gold
- SOCKS5: 248 alive / 160 gold

## Historical pool

- Discovered: 158911
- Ever alive: 30109
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
