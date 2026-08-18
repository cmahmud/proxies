# SyndProxy private pool

## Current pool

- Alive now: 857
- Gold now: 289
- HTTP: 272 alive / 25 gold
- HTTPS: 151 alive / 5 gold
- SOCKS4: 211 alive / 143 gold
- SOCKS5: 223 alive / 116 gold

## Historical pool

- Discovered: 102825
- Ever alive: 12783
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
