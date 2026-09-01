# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 471
- HTTP: 140 alive / 93 gold
- HTTPS: 124 alive / 42 gold
- SOCKS4: 184 alive / 163 gold
- SOCKS5: 200 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46958
- Ever gold: 1461

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
