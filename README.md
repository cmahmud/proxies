# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 418
- HTTP: 87 alive / 60 gold
- HTTPS: 81 alive / 23 gold
- SOCKS4: 178 alive / 167 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41540
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
