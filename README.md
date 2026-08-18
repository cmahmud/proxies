# SyndProxy private pool

## Current pool

- Alive now: 673
- Gold now: 247
- HTTP: 173 alive / 30 gold
- HTTPS: 91 alive / 10 gold
- SOCKS4: 221 alive / 118 gold
- SOCKS5: 188 alive / 89 gold

## Historical pool

- Discovered: 86739
- Ever alive: 6883
- Ever gold: 334

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
