# SyndProxy validated proxy pool

## Current pool

- Alive now: 1288
- Gold now: 0
- HTTP: 446 alive / 0 gold
- HTTPS: 135 alive / 0 gold
- SOCKS4: 343 alive / 0 gold
- SOCKS5: 364 alive / 0 gold

## Historical pool

- Discovered: 169115
- Ever alive: 32637
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
