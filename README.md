# SyndProxy private pool

## Current pool

- Alive now: 1096
- Gold now: 479
- HTTP: 395 alive / 131 gold
- HTTPS: 272 alive / 78 gold
- SOCKS4: 207 alive / 120 gold
- SOCKS5: 222 alive / 150 gold

## Historical pool

- Discovered: 119696
- Ever alive: 17874
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
