# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 437
- HTTP: 99 alive / 77 gold
- HTTPS: 55 alive / 28 gold
- SOCKS4: 191 alive / 164 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49125
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
