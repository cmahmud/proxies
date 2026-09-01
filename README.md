# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 436
- HTTP: 100 alive / 73 gold
- HTTPS: 100 alive / 31 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 185 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47327
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
