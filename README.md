# SyndProxy validated proxy pool

## Current pool

- Alive now: 682
- Gold now: 466
- HTTP: 149 alive / 97 gold
- HTTPS: 124 alive / 32 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 230 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46232
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
