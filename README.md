# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 380
- HTTP: 83 alive / 55 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 174 alive / 155 gold
- SOCKS5: 181 alive / 159 gold

## Historical pool

- Discovered: 174823
- Ever alive: 33105
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
