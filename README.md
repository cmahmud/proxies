# SyndProxy validated proxy pool

## Current pool

- Alive now: 656
- Gold now: 459
- HTTP: 130 alive / 95 gold
- HTTPS: 133 alive / 30 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 220 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46123
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
