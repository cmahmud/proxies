# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 461
- HTTP: 137 alive / 94 gold
- HTTPS: 123 alive / 33 gold
- SOCKS4: 184 alive / 160 gold
- SOCKS5: 205 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46397
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
