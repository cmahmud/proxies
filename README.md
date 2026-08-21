# SyndProxy private pool

## Current pool

- Alive now: 1026
- Gold now: 418
- HTTP: 303 alive / 93 gold
- HTTPS: 199 alive / 24 gold
- SOCKS4: 244 alive / 144 gold
- SOCKS5: 280 alive / 157 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28154
- Ever gold: 1107

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
