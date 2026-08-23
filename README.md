# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 371
- HTTP: 68 alive / 38 gold
- HTTPS: 36 alive / 12 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 175 alive / 161 gold

## Historical pool

- Discovered: 172867
- Ever alive: 32986
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
