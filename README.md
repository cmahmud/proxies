# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 429
- HTTP: 329 alive / 100 gold
- HTTPS: 229 alive / 22 gold
- SOCKS4: 241 alive / 144 gold
- SOCKS5: 278 alive / 163 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28170
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
