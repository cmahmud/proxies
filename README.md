# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 412
- HTTP: 110 alive / 73 gold
- HTTPS: 105 alive / 20 gold
- SOCKS4: 166 alive / 158 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41863
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
