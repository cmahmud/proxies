# SyndProxy private pool

## Current pool

- Alive now: 900
- Gold now: 426
- HTTP: 264 alive / 92 gold
- HTTPS: 194 alive / 28 gold
- SOCKS4: 205 alive / 146 gold
- SOCKS5: 237 alive / 160 gold

## Historical pool

- Discovered: 162751
- Ever alive: 31546
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
