# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 442
- HTTP: 116 alive / 84 gold
- HTTPS: 56 alive / 28 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49272
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
