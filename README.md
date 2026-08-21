# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 449
- HTTP: 350 alive / 113 gold
- HTTPS: 223 alive / 32 gold
- SOCKS4: 206 alive / 153 gold
- SOCKS5: 245 alive / 151 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28595
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
