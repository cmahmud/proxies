# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 360
- HTTP: 383 alive / 71 gold
- HTTPS: 238 alive / 13 gold
- SOCKS4: 212 alive / 129 gold
- SOCKS5: 251 alive / 147 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20366
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
