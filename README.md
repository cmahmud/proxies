# SyndProxy private pool

## Current pool

- Alive now: 940
- Gold now: 420
- HTTP: 319 alive / 107 gold
- HTTPS: 172 alive / 34 gold
- SOCKS4: 216 alive / 137 gold
- SOCKS5: 233 alive / 142 gold

## Historical pool

- Discovered: 160259
- Ever alive: 30718
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
