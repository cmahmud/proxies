# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 424
- HTTP: 115 alive / 77 gold
- HTTPS: 128 alive / 20 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42172
- Ever gold: 1353

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
