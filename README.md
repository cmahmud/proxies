# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 525
- HTTP: 367 alive / 157 gold
- HTTPS: 240 alive / 91 gold
- SOCKS4: 215 alive / 133 gold
- SOCKS5: 226 alive / 144 gold

## Historical pool

- Discovered: 122388
- Ever alive: 18688
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
