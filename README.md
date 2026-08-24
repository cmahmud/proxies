# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 389
- HTTP: 93 alive / 54 gold
- HTTPS: 46 alive / 12 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33348
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
