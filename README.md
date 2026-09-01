# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 456
- HTTP: 122 alive / 82 gold
- HTTPS: 119 alive / 33 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 191 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46755
- Ever gold: 1450

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
