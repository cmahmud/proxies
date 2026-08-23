# SyndProxy validated proxy pool

## Current pool

- Alive now: 449
- Gold now: 365
- HTTP: 74 alive / 46 gold
- HTTPS: 37 alive / 8 gold
- SOCKS4: 162 alive / 154 gold
- SOCKS5: 176 alive / 157 gold

## Historical pool

- Discovered: 173623
- Ever alive: 33018
- Ever gold: 1223

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
