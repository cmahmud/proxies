# SyndProxy private pool

## Current pool

- Alive now: 1245
- Gold now: 409
- HTTP: 430 alive / 80 gold
- HTTPS: 270 alive / 16 gold
- SOCKS4: 272 alive / 150 gold
- SOCKS5: 273 alive / 163 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20633
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
