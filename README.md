# SyndProxy private pool

## Current pool

- Alive now: 871
- Gold now: 339
- HTTP: 296 alive / 60 gold
- HTTPS: 194 alive / 13 gold
- SOCKS4: 196 alive / 142 gold
- SOCKS5: 185 alive / 124 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20199
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
