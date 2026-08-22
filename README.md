# SyndProxy private pool

## Current pool

- Alive now: 1057
- Gold now: 424
- HTTP: 303 alive / 90 gold
- HTTPS: 204 alive / 24 gold
- SOCKS4: 240 alive / 140 gold
- SOCKS5: 310 alive / 170 gold

## Historical pool

- Discovered: 164947
- Ever alive: 32217
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
