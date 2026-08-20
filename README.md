# SyndProxy private pool

## Current pool

- Alive now: 781
- Gold now: 365
- HTTP: 192 alive / 70 gold
- HTTPS: 140 alive / 22 gold
- SOCKS4: 223 alive / 147 gold
- SOCKS5: 226 alive / 126 gold

## Historical pool

- Discovered: 145547
- Ever alive: 25384
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
