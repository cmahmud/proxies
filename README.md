# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 405
- HTTP: 109 alive / 75 gold
- HTTPS: 61 alive / 18 gold
- SOCKS4: 170 alive / 153 gold
- SOCKS5: 180 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48091
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
