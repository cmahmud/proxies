# SyndProxy private pool

## Current pool

- Alive now: 795
- Gold now: 421
- HTTP: 202 alive / 88 gold
- HTTPS: 141 alive / 26 gold
- SOCKS4: 220 alive / 141 gold
- SOCKS5: 232 alive / 166 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27302
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
