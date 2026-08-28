# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 427
- HTTP: 103 alive / 76 gold
- HTTPS: 104 alive / 21 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42448
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
