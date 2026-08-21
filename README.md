# SyndProxy private pool

## Current pool

- Alive now: 1399
- Gold now: 459
- HTTP: 527 alive / 112 gold
- HTTPS: 362 alive / 33 gold
- SOCKS4: 244 alive / 153 gold
- SOCKS5: 266 alive / 161 gold

## Historical pool

- Discovered: 160009
- Ever alive: 30507
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
