# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 435
- HTTP: 103 alive / 74 gold
- HTTPS: 94 alive / 32 gold
- SOCKS4: 178 alive / 159 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47324
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
