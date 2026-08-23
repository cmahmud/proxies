# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 377
- HTTP: 93 alive / 56 gold
- HTTPS: 42 alive / 9 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 195 alive / 154 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33093
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
