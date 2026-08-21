# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 429
- HTTP: 303 alive / 109 gold
- HTTPS: 218 alive / 27 gold
- SOCKS4: 237 alive / 153 gold
- SOCKS5: 236 alive / 140 gold

## Historical pool

- Discovered: 160020
- Ever alive: 30540
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
