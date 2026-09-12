# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 436
- HTTP: 114 alive / 87 gold
- HTTPS: 52 alive / 31 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49437
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
