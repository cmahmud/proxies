# SyndProxy private pool

## Current pool

- Alive now: 974
- Gold now: 354
- HTTP: 321 alive / 58 gold
- HTTPS: 186 alive / 14 gold
- SOCKS4: 240 alive / 146 gold
- SOCKS5: 227 alive / 136 gold

## Historical pool

- Discovered: 107156
- Ever alive: 15133
- Ever gold: 483

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
