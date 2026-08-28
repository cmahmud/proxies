# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 390
- HTTP: 66 alive / 57 gold
- HTTPS: 67 alive / 13 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 174 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42861
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
