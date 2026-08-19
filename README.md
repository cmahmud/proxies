# SyndProxy private pool

## Current pool

- Alive now: 1127
- Gold now: 546
- HTTP: 409 alive / 169 gold
- HTTPS: 276 alive / 89 gold
- SOCKS4: 216 alive / 134 gold
- SOCKS5: 226 alive / 154 gold

## Historical pool

- Discovered: 123091
- Ever alive: 18745
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
