# SyndProxy private pool

## Current pool

- Alive now: 1220
- Gold now: 562
- HTTP: 464 alive / 185 gold
- HTTPS: 276 alive / 111 gold
- SOCKS4: 237 alive / 122 gold
- SOCKS5: 243 alive / 144 gold

## Historical pool

- Discovered: 124836
- Ever alive: 19283
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
