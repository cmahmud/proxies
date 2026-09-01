# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 436
- HTTP: 99 alive / 73 gold
- HTTPS: 103 alive / 30 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47328
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
