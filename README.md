# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 396
- HTTP: 93 alive / 66 gold
- HTTPS: 44 alive / 16 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 183 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48141
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
