# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 439
- HTTP: 99 alive / 72 gold
- HTTPS: 111 alive / 31 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47341
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
