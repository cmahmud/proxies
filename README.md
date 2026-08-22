# SyndProxy private pool

## Current pool

- Alive now: 837
- Gold now: 383
- HTTP: 253 alive / 97 gold
- HTTPS: 182 alive / 24 gold
- SOCKS4: 198 alive / 135 gold
- SOCKS5: 204 alive / 127 gold

## Historical pool

- Discovered: 162755
- Ever alive: 31579
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
