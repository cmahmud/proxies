# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 399
- HTTP: 324 alive / 90 gold
- HTTPS: 235 alive / 26 gold
- SOCKS4: 244 alive / 137 gold
- SOCKS5: 271 alive / 146 gold

## Historical pool

- Discovered: 164248
- Ever alive: 32109
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
