# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 426
- HTTP: 89 alive / 70 gold
- HTTPS: 76 alive / 23 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 181 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37971
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
