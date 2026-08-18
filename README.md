# SyndProxy private pool

## Current pool

- Alive now: 573
- Gold now: 225
- HTTP: 178 alive / 33 gold
- HTTPS: 87 alive / 10 gold
- SOCKS4: 151 alive / 105 gold
- SOCKS5: 157 alive / 77 gold

## Historical pool

- Discovered: 86653
- Ever alive: 5728
- Ever gold: 294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
