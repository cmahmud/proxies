# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 431
- HTTP: 105 alive / 79 gold
- HTTPS: 115 alive / 19 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 186 alive / 173 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42466
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
