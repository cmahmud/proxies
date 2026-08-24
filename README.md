# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 376
- HTTP: 126 alive / 52 gold
- HTTPS: 43 alive / 7 gold
- SOCKS4: 176 alive / 157 gold
- SOCKS5: 191 alive / 160 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33451
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
