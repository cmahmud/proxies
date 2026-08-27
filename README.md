# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 400
- HTTP: 74 alive / 51 gold
- HTTPS: 55 alive / 18 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41678
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
