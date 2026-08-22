# SyndProxy private pool

## Current pool

- Alive now: 839
- Gold now: 382
- HTTP: 237 alive / 88 gold
- HTTPS: 175 alive / 24 gold
- SOCKS4: 209 alive / 123 gold
- SOCKS5: 218 alive / 147 gold

## Historical pool

- Discovered: 163880
- Ever alive: 32035
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
