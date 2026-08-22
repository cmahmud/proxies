# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 374
- HTTP: 326 alive / 76 gold
- HTTPS: 234 alive / 28 gold
- SOCKS4: 191 alive / 130 gold
- SOCKS5: 227 alive / 140 gold

## Historical pool

- Discovered: 165755
- Ever alive: 32300
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
