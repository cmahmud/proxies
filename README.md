# SyndProxy validated proxy pool

## Current pool

- Alive now: 455
- Gold now: 370
- HTTP: 91 alive / 51 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 156 alive / 149 gold
- SOCKS5: 164 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43642
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
