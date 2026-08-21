# SyndProxy private pool

## Current pool

- Alive now: 774
- Gold now: 331
- HTTP: 222 alive / 77 gold
- HTTPS: 170 alive / 23 gold
- SOCKS4: 171 alive / 103 gold
- SOCKS5: 211 alive / 128 gold

## Historical pool

- Discovered: 157573
- Ever alive: 29771
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
