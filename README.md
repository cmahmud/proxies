# SyndProxy private pool

## Current pool

- Alive now: 795
- Gold now: 336
- HTTP: 237 alive / 78 gold
- HTTPS: 181 alive / 26 gold
- SOCKS4: 170 alive / 103 gold
- SOCKS5: 207 alive / 129 gold

## Historical pool

- Discovered: 157573
- Ever alive: 29773
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
