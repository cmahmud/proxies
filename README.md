# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 404
- HTTP: 89 alive / 59 gold
- HTTPS: 80 alive / 16 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41557
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
