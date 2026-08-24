# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 387
- HTTP: 97 alive / 55 gold
- HTTPS: 47 alive / 10 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33350
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
