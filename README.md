# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 424
- HTTP: 341 alive / 112 gold
- HTTPS: 215 alive / 31 gold
- SOCKS4: 231 alive / 144 gold
- SOCKS5: 242 alive / 137 gold

## Historical pool

- Discovered: 160276
- Ever alive: 30750
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
