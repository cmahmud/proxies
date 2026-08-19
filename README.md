# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 359
- HTTP: 332 alive / 65 gold
- HTTPS: 215 alive / 18 gold
- SOCKS4: 211 alive / 123 gold
- SOCKS5: 224 alive / 153 gold

## Historical pool

- Discovered: 109991
- Ever alive: 15655
- Ever gold: 499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
