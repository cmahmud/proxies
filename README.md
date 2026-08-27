# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 411
- HTTP: 113 alive / 64 gold
- HTTPS: 179 alive / 18 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40754
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
