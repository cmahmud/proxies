# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 412
- HTTP: 90 alive / 65 gold
- HTTPS: 96 alive / 21 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42651
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
