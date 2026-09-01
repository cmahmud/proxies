# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 433
- HTTP: 96 alive / 72 gold
- HTTPS: 104 alive / 30 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47333
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
