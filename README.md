# SyndProxy private pool

## Current pool

- Alive now: 747
- Gold now: 383
- HTTP: 248 alive / 68 gold
- HTTPS: 101 alive / 19 gold
- SOCKS4: 187 alive / 149 gold
- SOCKS5: 211 alive / 147 gold

## Historical pool

- Discovered: 146664
- Ever alive: 25748
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
