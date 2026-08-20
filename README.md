# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 410
- HTTP: 290 alive / 92 gold
- HTTPS: 202 alive / 27 gold
- SOCKS4: 213 alive / 136 gold
- SOCKS5: 226 alive / 155 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27602
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
