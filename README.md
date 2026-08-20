# SyndProxy private pool

## Current pool

- Alive now: 713
- Gold now: 394
- HTTP: 180 alive / 71 gold
- HTTPS: 123 alive / 19 gold
- SOCKS4: 199 alive / 150 gold
- SOCKS5: 211 alive / 154 gold

## Historical pool

- Discovered: 147183
- Ever alive: 25814
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
