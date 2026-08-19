# SyndProxy private pool

## Current pool

- Alive now: 1140
- Gold now: 546
- HTTP: 417 alive / 169 gold
- HTTPS: 278 alive / 89 gold
- SOCKS4: 218 alive / 134 gold
- SOCKS5: 227 alive / 154 gold

## Historical pool

- Discovered: 123091
- Ever alive: 18745
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
