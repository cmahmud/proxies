# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 399
- HTTP: 75 alive / 53 gold
- HTTPS: 53 alive / 19 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41682
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
