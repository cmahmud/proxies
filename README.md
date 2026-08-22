# SyndProxy private pool

## Current pool

- Alive now: 789
- Gold now: 341
- HTTP: 238 alive / 78 gold
- HTTPS: 155 alive / 24 gold
- SOCKS4: 179 alive / 113 gold
- SOCKS5: 217 alive / 126 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32579
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
