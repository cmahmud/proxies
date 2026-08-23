# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 385
- HTTP: 96 alive / 61 gold
- HTTPS: 45 alive / 11 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 187 alive / 157 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33089
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
