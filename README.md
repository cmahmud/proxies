# SyndProxy private pool

## Current pool

- Alive now: 939
- Gold now: 401
- HTTP: 306 alive / 96 gold
- HTTPS: 187 alive / 25 gold
- SOCKS4: 236 alive / 144 gold
- SOCKS5: 210 alive / 136 gold

## Historical pool

- Discovered: 165824
- Ever alive: 32343
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
