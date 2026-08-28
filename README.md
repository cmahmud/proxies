# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 393
- HTTP: 79 alive / 52 gold
- HTTPS: 65 alive / 18 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 177 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42874
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
