# SyndProxy private pool

## Current pool

- Alive now: 691
- Gold now: 189
- HTTP: 185 alive / 34 gold
- HTTPS: 113 alive / 10 gold
- SOCKS4: 222 alive / 77 gold
- SOCKS5: 171 alive / 68 gold

## Historical pool

- Discovered: 82934
- Ever alive: 5060
- Ever gold: 259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
