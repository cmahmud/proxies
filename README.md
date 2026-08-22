# SyndProxy private pool

## Current pool

- Alive now: 958
- Gold now: 373
- HTTP: 306 alive / 79 gold
- HTTPS: 230 alive / 25 gold
- SOCKS4: 167 alive / 105 gold
- SOCKS5: 255 alive / 164 gold

## Historical pool

- Discovered: 166635
- Ever alive: 32473
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
