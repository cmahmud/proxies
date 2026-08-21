# SyndProxy private pool

## Current pool

- Alive now: 820
- Gold now: 394
- HTTP: 226 alive / 87 gold
- HTTPS: 163 alive / 19 gold
- SOCKS4: 195 alive / 130 gold
- SOCKS5: 236 alive / 158 gold

## Historical pool

- Discovered: 151681
- Ever alive: 27666
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
