# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 373
- HTTP: 96 alive / 47 gold
- HTTPS: 38 alive / 11 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 189 alive / 160 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32962
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
