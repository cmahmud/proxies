# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 462
- HTTP: 129 alive / 96 gold
- HTTPS: 124 alive / 31 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 216 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46127
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
