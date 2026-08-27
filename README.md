# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 408
- HTTP: 92 alive / 60 gold
- HTTPS: 88 alive / 18 gold
- SOCKS4: 178 alive / 165 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41546
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
