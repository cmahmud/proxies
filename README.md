# SyndProxy validated proxy pool

## Current pool

- Alive now: 658
- Gold now: 473
- HTTP: 146 alive / 95 gold
- HTTPS: 126 alive / 41 gold
- SOCKS4: 185 alive / 163 gold
- SOCKS5: 201 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46958
- Ever gold: 1461

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
