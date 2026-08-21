# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 420
- HTTP: 307 alive / 107 gold
- HTTPS: 177 alive / 34 gold
- SOCKS4: 218 alive / 136 gold
- SOCKS5: 226 alive / 143 gold

## Historical pool

- Discovered: 160259
- Ever alive: 30722
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
