# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 311
- HTTP: 337 alive / 33 gold
- HTTPS: 168 alive / 5 gold
- SOCKS4: 226 alive / 144 gold
- SOCKS5: 219 alive / 129 gold

## Historical pool

- Discovered: 102848
- Ever alive: 13333
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
