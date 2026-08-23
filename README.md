# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 385
- HTTP: 112 alive / 61 gold
- HTTPS: 42 alive / 10 gold
- SOCKS4: 175 alive / 156 gold
- SOCKS5: 195 alive / 158 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33088
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
