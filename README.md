# SyndProxy private pool

## Current pool

- Alive now: 948
- Gold now: 334
- HTTP: 340 alive / 84 gold
- HTTPS: 206 alive / 19 gold
- SOCKS4: 209 alive / 141 gold
- SOCKS5: 193 alive / 90 gold

## Historical pool

- Discovered: 167096
- Ever alive: 32490
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
