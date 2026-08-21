# SyndProxy private pool

## Current pool

- Alive now: 1378
- Gold now: 427
- HTTP: 541 alive / 101 gold
- HTTPS: 368 alive / 28 gold
- SOCKS4: 223 alive / 140 gold
- SOCKS5: 246 alive / 158 gold

## Historical pool

- Discovered: 159279
- Ever alive: 30404
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
