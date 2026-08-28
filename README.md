# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 414
- HTTP: 105 alive / 68 gold
- HTTPS: 97 alive / 21 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 177 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42616
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
