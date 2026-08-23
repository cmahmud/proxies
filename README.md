# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 374
- HTTP: 101 alive / 49 gold
- HTTPS: 45 alive / 13 gold
- SOCKS4: 170 alive / 155 gold
- SOCKS5: 197 alive / 157 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32958
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
