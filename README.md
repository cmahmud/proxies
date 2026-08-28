# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 395
- HTTP: 78 alive / 55 gold
- HTTPS: 45 alive / 15 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 174 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42840
- Ever gold: 1362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
