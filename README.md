# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 428
- HTTP: 103 alive / 76 gold
- HTTPS: 115 alive / 21 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42448
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
