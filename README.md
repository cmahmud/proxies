# SyndProxy private pool

## Current pool

- Alive now: 1558
- Gold now: 607
- HTTP: 588 alive / 196 gold
- HTTPS: 485 alive / 83 gold
- SOCKS4: 233 alive / 154 gold
- SOCKS5: 252 alive / 174 gold

## Historical pool

- Discovered: 141227
- Ever alive: 23986
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
