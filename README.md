# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 387
- HTTP: 93 alive / 52 gold
- HTTPS: 37 alive / 13 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 194 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33345
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
