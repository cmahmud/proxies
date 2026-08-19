# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 583
- HTTP: 363 alive / 171 gold
- HTTPS: 299 alive / 143 gold
- SOCKS4: 216 alive / 143 gold
- SOCKS5: 203 alive / 126 gold

## Historical pool

- Discovered: 127380
- Ever alive: 19960
- Ever gold: 861

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
