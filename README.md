# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 424
- HTTP: 309 alive / 92 gold
- HTTPS: 220 alive / 22 gold
- SOCKS4: 200 alive / 147 gold
- SOCKS5: 246 alive / 163 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28782
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
