# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 372
- HTTP: 313 alive / 78 gold
- HTTPS: 250 alive / 26 gold
- SOCKS4: 181 alive / 125 gold
- SOCKS5: 227 alive / 143 gold

## Historical pool

- Discovered: 165755
- Ever alive: 32306
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
