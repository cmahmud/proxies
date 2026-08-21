# SyndProxy private pool

## Current pool

- Alive now: 860
- Gold now: 368
- HTTP: 291 alive / 103 gold
- HTTPS: 155 alive / 27 gold
- SOCKS4: 202 alive / 133 gold
- SOCKS5: 212 alive / 105 gold

## Historical pool

- Discovered: 154710
- Ever alive: 28964
- Ever gold: 1117

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
