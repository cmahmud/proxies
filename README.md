# SyndProxy private pool

## Current pool

- Alive now: 1244
- Gold now: 190
- HTTP: 514 alive / 36 gold
- HTTPS: 271 alive / 10 gold
- SOCKS4: 262 alive / 76 gold
- SOCKS5: 197 alive / 68 gold

## Historical pool

- Discovered: 82934
- Ever alive: 5060
- Ever gold: 259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
