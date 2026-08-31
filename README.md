# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 451
- HTTP: 144 alive / 82 gold
- HTTPS: 107 alive / 34 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 222 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45436
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
