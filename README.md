# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 431
- HTTP: 112 alive / 78 gold
- HTTPS: 66 alive / 22 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34108
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
