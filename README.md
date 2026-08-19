# SyndProxy private pool

## Current pool

- Alive now: 1118
- Gold now: 534
- HTTP: 402 alive / 161 gold
- HTTPS: 272 alive / 84 gold
- SOCKS4: 234 alive / 150 gold
- SOCKS5: 210 alive / 139 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18046
- Ever gold: 713

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
