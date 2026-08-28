# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 390
- HTTP: 77 alive / 54 gold
- HTTPS: 63 alive / 13 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 172 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42900
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
