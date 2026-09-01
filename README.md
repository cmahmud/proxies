# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 477
- HTTP: 148 alive / 99 gold
- HTTPS: 124 alive / 39 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 195 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46946
- Ever gold: 1458

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
