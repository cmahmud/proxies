# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 380
- HTTP: 95 alive / 59 gold
- HTTPS: 46 alive / 11 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 183 alive / 154 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33091
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
