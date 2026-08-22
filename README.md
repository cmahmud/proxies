# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 380
- HTTP: 355 alive / 79 gold
- HTTPS: 238 alive / 24 gold
- SOCKS4: 220 alive / 124 gold
- SOCKS5: 236 alive / 153 gold

## Historical pool

- Discovered: 164970
- Ever alive: 32247
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
