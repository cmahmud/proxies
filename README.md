# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 418
- HTTP: 103 alive / 58 gold
- HTTPS: 96 alive / 23 gold
- SOCKS4: 181 alive / 168 gold
- SOCKS5: 194 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41538
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
