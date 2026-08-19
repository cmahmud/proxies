# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 534
- HTTP: 371 alive / 154 gold
- HTTPS: 259 alive / 107 gold
- SOCKS4: 208 alive / 144 gold
- SOCKS5: 202 alive / 129 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19914
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
