# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 390
- HTTP: 73 alive / 57 gold
- HTTPS: 69 alive / 13 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 174 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42864
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
