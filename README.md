# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 389
- HTTP: 108 alive / 55 gold
- HTTPS: 52 alive / 10 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 194 alive / 164 gold

## Historical pool

- Discovered: 178001
- Ever alive: 33358
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
