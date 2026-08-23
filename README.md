# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 373
- HTTP: 84 alive / 45 gold
- HTTPS: 46 alive / 12 gold
- SOCKS4: 169 alive / 155 gold
- SOCKS5: 192 alive / 161 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32963
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
