# SyndProxy private pool

## Current pool

- Alive now: 856
- Gold now: 395
- HTTP: 254 alive / 91 gold
- HTTPS: 178 alive / 14 gold
- SOCKS4: 221 alive / 157 gold
- SOCKS5: 203 alive / 133 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18242
- Ever gold: 717

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
