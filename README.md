# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 418
- HTTP: 342 alive / 91 gold
- HTTPS: 222 alive / 30 gold
- SOCKS4: 235 alive / 144 gold
- SOCKS5: 254 alive / 153 gold

## Historical pool

- Discovered: 164927
- Ever alive: 32165
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
