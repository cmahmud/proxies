# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 380
- HTTP: 106 alive / 60 gold
- HTTPS: 34 alive / 9 gold
- SOCKS4: 170 alive / 153 gold
- SOCKS5: 186 alive / 158 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33086
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
