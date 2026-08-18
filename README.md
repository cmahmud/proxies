# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 344
- HTTP: 336 alive / 50 gold
- HTTPS: 211 alive / 14 gold
- SOCKS4: 230 alive / 143 gold
- SOCKS5: 231 alive / 137 gold

## Historical pool

- Discovered: 107145
- Ever alive: 15096
- Ever gold: 479

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
