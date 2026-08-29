# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 378
- HTTP: 91 alive / 58 gold
- HTTPS: 51 alive / 20 gold
- SOCKS4: 154 alive / 151 gold
- SOCKS5: 161 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43646
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
