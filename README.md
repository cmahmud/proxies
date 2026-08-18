# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 286
- HTTP: 364 alive / 29 gold
- HTTPS: 163 alive / 6 gold
- SOCKS4: 254 alive / 128 gold
- SOCKS5: 250 alive / 123 gold

## Historical pool

- Discovered: 102839
- Ever alive: 13122
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
