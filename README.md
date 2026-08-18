# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 296
- HTTP: 219 alive / 29 gold
- HTTPS: 124 alive / 5 gold
- SOCKS4: 258 alive / 144 gold
- SOCKS5: 243 alive / 118 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12157
- Ever gold: 395

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
