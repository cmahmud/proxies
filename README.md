# SyndProxy validated proxy pool

## Current pool

- Alive now: 437
- Gold now: 360
- HTTP: 70 alive / 52 gold
- HTTPS: 31 alive / 13 gold
- SOCKS4: 164 alive / 150 gold
- SOCKS5: 172 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48255
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
