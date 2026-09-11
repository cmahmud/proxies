# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 436
- HTTP: 97 alive / 77 gold
- HTTPS: 54 alive / 27 gold
- SOCKS4: 188 alive / 164 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49128
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
