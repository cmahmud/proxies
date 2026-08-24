# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 387
- HTTP: 97 alive / 59 gold
- HTTPS: 46 alive / 16 gold
- SOCKS4: 169 alive / 154 gold
- SOCKS5: 178 alive / 158 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33504
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
