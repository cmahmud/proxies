# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 433
- HTTP: 97 alive / 71 gold
- HTTPS: 103 alive / 29 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47334
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
