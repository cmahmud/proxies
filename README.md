# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 420
- HTTP: 102 alive / 72 gold
- HTTPS: 112 alive / 18 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42536
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
