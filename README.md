# SyndProxy private pool

## Current pool

- Alive now: 731
- Gold now: 376
- HTTP: 213 alive / 69 gold
- HTTPS: 126 alive / 18 gold
- SOCKS4: 186 alive / 144 gold
- SOCKS5: 206 alive / 145 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25831
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
