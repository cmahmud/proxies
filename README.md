# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 428
- HTTP: 90 alive / 74 gold
- HTTPS: 60 alive / 25 gold
- SOCKS4: 186 alive / 168 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49091
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
