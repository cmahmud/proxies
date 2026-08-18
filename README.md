# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 280
- HTTP: 283 alive / 40 gold
- HTTPS: 182 alive / 8 gold
- SOCKS4: 214 alive / 140 gold
- SOCKS5: 165 alive / 92 gold

## Historical pool

- Discovered: 102887
- Ever alive: 13788
- Ever gold: 430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
