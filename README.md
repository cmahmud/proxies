# SyndProxy private pool

## Current pool

- Alive now: 1347
- Gold now: 551
- HTTP: 501 alive / 180 gold
- HTTPS: 367 alive / 82 gold
- SOCKS4: 239 alive / 131 gold
- SOCKS5: 240 alive / 158 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22977
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
