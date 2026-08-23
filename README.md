# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 373
- HTTP: 88 alive / 57 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 168 alive / 150 gold
- SOCKS5: 188 alive / 155 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33101
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
