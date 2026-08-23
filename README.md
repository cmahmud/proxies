# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 373
- HTTP: 99 alive / 49 gold
- HTTPS: 54 alive / 12 gold
- SOCKS4: 177 alive / 155 gold
- SOCKS5: 202 alive / 157 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32958
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
