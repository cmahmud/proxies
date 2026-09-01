# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 467
- HTTP: 148 alive / 95 gold
- HTTPS: 128 alive / 34 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46326
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
