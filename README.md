# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 412
- HTTP: 93 alive / 66 gold
- HTTPS: 88 alive / 19 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 192 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42685
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
