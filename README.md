# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 435
- HTTP: 102 alive / 73 gold
- HTTPS: 96 alive / 31 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 184 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47326
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
