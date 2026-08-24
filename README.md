# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 387
- HTTP: 100 alive / 60 gold
- HTTPS: 45 alive / 15 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 178 alive / 157 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33504
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
