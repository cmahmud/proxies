# SyndProxy private pool

## Current pool

- Alive now: 855
- Gold now: 402
- HTTP: 249 alive / 81 gold
- HTTPS: 190 alive / 23 gold
- SOCKS4: 207 alive / 147 gold
- SOCKS5: 209 alive / 151 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27165
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
