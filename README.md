# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 379
- HTTP: 88 alive / 61 gold
- HTTPS: 32 alive / 10 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 179 alive / 155 gold

## Historical pool

- Discovered: 174811
- Ever alive: 33096
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
