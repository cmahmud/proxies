# SyndProxy private pool

## Current pool

- Alive now: 1412
- Gold now: 444
- HTTP: 527 alive / 102 gold
- HTTPS: 364 alive / 28 gold
- SOCKS4: 249 alive / 152 gold
- SOCKS5: 272 alive / 162 gold

## Historical pool

- Discovered: 159335
- Ever alive: 30475
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
