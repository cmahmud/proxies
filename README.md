# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 393
- HTTP: 92 alive / 59 gold
- HTTPS: 42 alive / 11 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 192 alive / 164 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33343
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
