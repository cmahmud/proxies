# SyndProxy private pool

## Current pool

- Alive now: 781
- Gold now: 410
- HTTP: 207 alive / 88 gold
- HTTPS: 145 alive / 28 gold
- SOCKS4: 191 alive / 138 gold
- SOCKS5: 238 alive / 156 gold

## Historical pool

- Discovered: 163376
- Ever alive: 31908
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
