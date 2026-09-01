# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 433
- HTTP: 91 alive / 70 gold
- HTTPS: 95 alive / 30 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47328
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
