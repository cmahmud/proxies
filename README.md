# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 458
- HTTP: 124 alive / 83 gold
- HTTPS: 52 alive / 32 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 199 alive / 179 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49230
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
