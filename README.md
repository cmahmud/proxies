# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 419
- HTTP: 93 alive / 69 gold
- HTTPS: 101 alive / 19 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42493
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
