# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 411
- HTTP: 373 alive / 96 gold
- HTTPS: 255 alive / 33 gold
- SOCKS4: 212 alive / 146 gold
- SOCKS5: 241 alive / 136 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30969
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
