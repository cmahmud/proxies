# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 371
- HTTP: 97 alive / 46 gold
- HTTPS: 36 alive / 10 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 184 alive / 160 gold

## Historical pool

- Discovered: 173048
- Ever alive: 32990
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
