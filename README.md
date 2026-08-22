# SyndProxy private pool

## Current pool

- Alive now: 953
- Gold now: 424
- HTTP: 309 alive / 92 gold
- HTTPS: 189 alive / 27 gold
- SOCKS4: 209 alive / 147 gold
- SOCKS5: 246 alive / 158 gold

## Historical pool

- Discovered: 162751
- Ever alive: 31553
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
