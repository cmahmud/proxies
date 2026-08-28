# SyndProxy validated proxy pool

## Current pool

- Alive now: 454
- Gold now: 402
- HTTP: 72 alive / 56 gold
- HTTPS: 36 alive / 18 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 177 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42856
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
