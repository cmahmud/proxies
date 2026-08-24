# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 402
- HTTP: 159 alive / 67 gold
- HTTPS: 47 alive / 12 gold
- SOCKS4: 193 alive / 159 gold
- SOCKS5: 207 alive / 164 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33333
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
