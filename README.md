# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 420
- HTTP: 97 alive / 70 gold
- HTTPS: 105 alive / 19 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42493
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
