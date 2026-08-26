# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 389
- HTTP: 134 alive / 70 gold
- HTTPS: 164 alive / 23 gold
- SOCKS4: 162 alive / 146 gold
- SOCKS5: 179 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39815
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
