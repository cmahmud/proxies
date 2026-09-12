# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 443
- HTTP: 115 alive / 83 gold
- HTTPS: 57 alive / 29 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49272
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
