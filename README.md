# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 434
- HTTP: 99 alive / 78 gold
- HTTPS: 56 alive / 27 gold
- SOCKS4: 186 alive / 168 gold
- SOCKS5: 181 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49092
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
