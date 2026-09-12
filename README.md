# SyndProxy validated proxy pool

## Current pool

- Alive now: 384
- Gold now: 326
- HTTP: 81 alive / 67 gold
- HTTPS: 31 alive / 21 gold
- SOCKS4: 129 alive / 111 gold
- SOCKS5: 143 alive / 127 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49547
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
