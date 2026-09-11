# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 362
- HTTP: 103 alive / 71 gold
- HTTPS: 55 alive / 22 gold
- SOCKS4: 121 alive / 99 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48712
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
