# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 417
- HTTP: 93 alive / 62 gold
- HTTPS: 81 alive / 23 gold
- SOCKS4: 180 alive / 166 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41542
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
