# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 386
- HTTP: 113 alive / 61 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 177 alive / 156 gold
- SOCKS5: 196 alive / 159 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33088
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
