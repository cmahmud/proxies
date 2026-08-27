# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 414
- HTTP: 105 alive / 69 gold
- HTTPS: 111 alive / 17 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 194 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41407
- Ever gold: 1327

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
