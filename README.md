# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 422
- HTTP: 105 alive / 69 gold
- HTTPS: 33 alive / 18 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 188 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48964
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
