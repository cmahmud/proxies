# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 195
- HTTP: 337 alive / 24 gold
- HTTPS: 117 alive / 7 gold
- SOCKS4: 182 alive / 97 gold
- SOCKS5: 198 alive / 67 gold

## Historical pool

- Discovered: 91526
- Ever alive: 8273
- Ever gold: 347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
