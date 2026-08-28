# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 356
- HTTP: 71 alive / 51 gold
- HTTPS: 39 alive / 17 gold
- SOCKS4: 166 alive / 137 gold
- SOCKS5: 175 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42858
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
