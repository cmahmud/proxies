# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 392
- HTTP: 97 alive / 62 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33317
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
