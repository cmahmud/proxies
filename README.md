# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 407
- HTTP: 82 alive / 58 gold
- HTTPS: 105 alive / 23 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 171 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42975
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
