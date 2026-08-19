# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 515
- HTTP: 345 alive / 161 gold
- HTTPS: 272 alive / 91 gold
- SOCKS4: 217 alive / 142 gold
- SOCKS5: 211 alive / 121 gold

## Historical pool

- Discovered: 119842
- Ever alive: 18369
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
