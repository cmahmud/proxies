# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 434
- HTTP: 98 alive / 76 gold
- HTTPS: 50 alive / 28 gold
- SOCKS4: 186 alive / 161 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49143
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
