# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 430
- HTTP: 91 alive / 75 gold
- HTTPS: 59 alive / 25 gold
- SOCKS4: 186 alive / 168 gold
- SOCKS5: 177 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49091
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
