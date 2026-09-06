# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 396
- HTTP: 127 alive / 82 gold
- HTTPS: 54 alive / 23 gold
- SOCKS4: 155 alive / 137 gold
- SOCKS5: 185 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48029
- Ever gold: 1513

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
