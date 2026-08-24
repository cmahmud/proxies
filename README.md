# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 391
- HTTP: 89 alive / 59 gold
- HTTPS: 42 alive / 10 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 194 alive / 164 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33343
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
