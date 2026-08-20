# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 381
- HTTP: 223 alive / 79 gold
- HTTPS: 194 alive / 19 gold
- SOCKS4: 202 alive / 147 gold
- SOCKS5: 217 alive / 136 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26846
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
