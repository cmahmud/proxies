# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 440
- HTTP: 279 alive / 85 gold
- HTTPS: 223 alive / 29 gold
- SOCKS4: 232 alive / 156 gold
- SOCKS5: 255 alive / 170 gold

## Historical pool

- Discovered: 163873
- Ever alive: 32015
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
