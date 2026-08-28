# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 405
- HTTP: 79 alive / 57 gold
- HTTPS: 88 alive / 22 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 176 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42958
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
