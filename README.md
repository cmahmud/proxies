# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 433
- HTTP: 103 alive / 74 gold
- HTTPS: 93 alive / 31 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47322
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
