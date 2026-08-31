# SyndProxy validated proxy pool

## Current pool

- Alive now: 705
- Gold now: 461
- HTTP: 151 alive / 95 gold
- HTTPS: 129 alive / 29 gold
- SOCKS4: 181 alive / 163 gold
- SOCKS5: 244 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46263
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
