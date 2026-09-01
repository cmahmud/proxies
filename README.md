# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 474
- HTTP: 147 alive / 97 gold
- HTTPS: 123 alive / 41 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 201 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46956
- Ever gold: 1461

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
