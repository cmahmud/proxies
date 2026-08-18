# SyndProxy private pool

## Current pool

- Alive now: 598
- Gold now: 194
- HTTP: 146 alive / 20 gold
- HTTPS: 93 alive / 8 gold
- SOCKS4: 168 alive / 97 gold
- SOCKS5: 191 alive / 69 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8006
- Ever gold: 346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
