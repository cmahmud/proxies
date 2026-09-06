# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 360
- HTTP: 79 alive / 46 gold
- HTTPS: 31 alive / 10 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 177 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48309
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
