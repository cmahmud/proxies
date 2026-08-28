# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 395
- HTTP: 76 alive / 53 gold
- HTTPS: 40 alive / 17 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42855
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
