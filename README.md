# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 446
- HTTP: 241 alive / 98 gold
- HTTPS: 184 alive / 32 gold
- SOCKS4: 230 alive / 151 gold
- SOCKS5: 259 alive / 165 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31808
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
