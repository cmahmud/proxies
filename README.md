# SyndProxy private pool

## Current pool

- Alive now: 1170
- Gold now: 400
- HTTP: 391 alive / 102 gold
- HTTPS: 275 alive / 25 gold
- SOCKS4: 201 alive / 129 gold
- SOCKS5: 303 alive / 144 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22612
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
