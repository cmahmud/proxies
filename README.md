# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 370
- HTTP: 82 alive / 45 gold
- HTTPS: 37 alive / 10 gold
- SOCKS4: 181 alive / 155 gold
- SOCKS5: 186 alive / 160 gold

## Historical pool

- Discovered: 173048
- Ever alive: 32990
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
