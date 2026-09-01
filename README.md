# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 429
- HTTP: 117 alive / 71 gold
- HTTPS: 68 alive / 30 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 174 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47055
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
