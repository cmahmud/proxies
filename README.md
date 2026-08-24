# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 387
- HTTP: 109 alive / 58 gold
- HTTPS: 51 alive / 10 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 177586
- Ever alive: 33321
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
