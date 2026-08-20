# SyndProxy private pool

## Current pool

- Alive now: 1529
- Gold now: 588
- HTTP: 537 alive / 195 gold
- HTTPS: 456 alive / 92 gold
- SOCKS4: 244 alive / 144 gold
- SOCKS5: 292 alive / 157 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24050
- Ever gold: 968

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
