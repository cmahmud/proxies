# SyndProxy private pool

## Current pool

- Alive now: 742
- Gold now: 385
- HTTP: 178 alive / 88 gold
- HTTPS: 151 alive / 26 gold
- SOCKS4: 201 alive / 127 gold
- SOCKS5: 212 alive / 144 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27293
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
