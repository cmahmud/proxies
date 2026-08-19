# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 353
- HTTP: 284 alive / 69 gold
- HTTPS: 229 alive / 18 gold
- SOCKS4: 252 alive / 155 gold
- SOCKS5: 221 alive / 111 gold

## Historical pool

- Discovered: 110865
- Ever alive: 15966
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
