# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 527
- HTTP: 375 alive / 159 gold
- HTTPS: 243 alive / 91 gold
- SOCKS4: 214 alive / 133 gold
- SOCKS5: 226 alive / 144 gold

## Historical pool

- Discovered: 122388
- Ever alive: 18690
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
