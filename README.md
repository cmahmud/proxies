# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 433
- HTTP: 100 alive / 73 gold
- HTTPS: 98 alive / 31 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47325
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
