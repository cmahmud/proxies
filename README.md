# SyndProxy private pool

## Current pool

- Alive now: 724
- Gold now: 391
- HTTP: 186 alive / 88 gold
- HTTPS: 122 alive / 17 gold
- SOCKS4: 207 alive / 136 gold
- SOCKS5: 209 alive / 150 gold

## Historical pool

- Discovered: 155381
- Ever alive: 29188
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
