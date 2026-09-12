# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 442
- HTTP: 115 alive / 87 gold
- HTTPS: 50 alive / 26 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 186 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49270
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
