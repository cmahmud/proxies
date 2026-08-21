# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 441
- HTTP: 315 alive / 94 gold
- HTTPS: 246 alive / 26 gold
- SOCKS4: 232 alive / 151 gold
- SOCKS5: 249 alive / 170 gold

## Historical pool

- Discovered: 158929
- Ever alive: 30156
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
