# SyndProxy private pool

## Current pool

- Alive now: 801
- Gold now: 353
- HTTP: 252 alive / 84 gold
- HTTPS: 149 alive / 21 gold
- SOCKS4: 189 alive / 119 gold
- SOCKS5: 211 alive / 129 gold

## Historical pool

- Discovered: 167449
- Ever alive: 32586
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
