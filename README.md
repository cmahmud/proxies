# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 380
- HTTP: 100 alive / 60 gold
- HTTPS: 44 alive / 9 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 182 alive / 155 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33093
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
