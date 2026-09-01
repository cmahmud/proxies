# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 417
- HTTP: 89 alive / 60 gold
- HTTPS: 38 alive / 25 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47091
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
