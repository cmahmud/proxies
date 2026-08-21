# SyndProxy private pool

## Current pool

- Alive now: 960
- Gold now: 424
- HTTP: 309 alive / 90 gold
- HTTPS: 209 alive / 22 gold
- SOCKS4: 195 alive / 147 gold
- SOCKS5: 247 alive / 165 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28770
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
