# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 442
- HTTP: 100 alive / 82 gold
- HTTPS: 55 alive / 30 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49195
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
