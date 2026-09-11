# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 447
- HTTP: 111 alive / 80 gold
- HTTPS: 50 alive / 31 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49214
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
