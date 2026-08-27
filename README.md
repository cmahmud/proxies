# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 398
- HTTP: 80 alive / 53 gold
- HTTPS: 51 alive / 20 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41684
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
