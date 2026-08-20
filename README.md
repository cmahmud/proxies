# SyndProxy private pool

## Current pool

- Alive now: 1267
- Gold now: 428
- HTTP: 453 alive / 102 gold
- HTTPS: 291 alive / 24 gold
- SOCKS4: 212 alive / 144 gold
- SOCKS5: 311 alive / 158 gold

## Historical pool

- Discovered: 136246
- Ever alive: 22640
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
