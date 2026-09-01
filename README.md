# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 440
- HTTP: 99 alive / 73 gold
- HTTPS: 106 alive / 31 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 192 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47339
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
